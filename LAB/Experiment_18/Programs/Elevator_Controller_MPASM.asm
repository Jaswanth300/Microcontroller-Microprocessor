; ==============================================================================
; Experiment 18: Multi-Floor Elevator Controller (Assembly Implementation)
; Target: PIC18F45K22 (MPASM)
; Author: Naga Jaswanth (Reg. No: 192424300)
; ==============================================================================

#include <p18f45k22.inc>

#define STEPS_PER_FLOOR D'200'
#define UP_LED 0
#define DOWN_LED 1
#define DOOR_LED 2

UDATA_ACS
floor_now res 1
req res 1
direction res 1
ph res 1
mv_dir res 1
s_cnt res 1
i_cnt res 1
t_cnt res 1
dly_cnt res 1
cnt_h res 1
cnt_l res 1

ORG 0x0000
goto Main

seg_tab:
    addwf PCL, F
    retlw 0x3F ; Floor 0
    retlw 0x06 ; Floor 1
    retlw 0x5B ; Floor 2
    retlw 0x4F ; Floor 3

phase_tab:
    addwf PCL, F
    retlw 0x09
    retlw 0x0C
    retlw 0x06
    retlw 0x03

bit_mask_tab:
    addwf PCL, F
    retlw 0x01
    retlw 0x02
    retlw 0x04
    retlw 0x08

above_mask_tab:
    addwf PCL, F
    retlw 0x0E
    retlw 0x0C
    retlw 0x08
    retlw 0x00

below_mask_tab:
    addwf PCL, F
    retlw 0x00
    retlw 0x01
    retlw 0x03
    retlw 0x07

delay_1ms:
    movlw D'76'
    movwf dly_cnt
DLY_LOOP:
    decfsz dly_cnt, F
    bra DLY_LOOP
    return

delay_ms:
    movwf t_cnt
DMS_LOOP:
    call delay_1ms
    call delay_1ms
    call delay_1ms
    call delay_1ms
    decfsz t_cnt, F
    bra DMS_LOOP
    return

step_motor:
    movf mv_dir, F
    bz SM_DOWN
    incf ph, F
    bra SM_OUT
SM_DOWN:
    decf ph, F
SM_OUT:
    movlw 0x03
    andwf ph, F
    movf ph, W
    call phase_tab
    movwf LATD
    movlw D'2'
    call delay_ms
    return

move_floor:
    movlw STEPS_PER_FLOOR
    movwf s_cnt
MF_LOOP:
    call step_motor
    decfsz s_cnt, F
    bra MF_LOOP
    return

show_floor:
    movf floor_now, W
    call seg_tab
    movwf LATC
    return

open_door:
    bsf LATB, DOOR_LED
    movlw D'4'
    movwf i_cnt
OD_LOOP:
    movlw D'250'
    call delay_ms
    decfsz i_cnt, F
    bra OD_LOOP
    bcf LATB, DOOR_LED
    return

Main:
    movlw 0x07
    movwf ADCON1
    clrf TRISB
    movlw 0x0F
    movwf TRISC
    clrf TRISD
    clrf floor_now
    clrf req
    clrf direction
    clrf ph
    clrf mv_dir
    clrf LATB
    clrf LATD
    call show_floor

MainLoop:
    movf PORTC, W
    xorlw 0xFF
    andlw 0x0F
    iorwf req, F
    movf req, F
    bz MainLoop

    movf floor_now, W
    call bit_mask_tab
    andwf req, W
    bz NotHere

    movf floor_now, W
    call bit_mask_tab
    xorlw 0xFF
    andwf req, F
    call open_door
    bra MainLoop

NotHere:
    movf floor_now, W
    call above_mask_tab
    andwf req, W
    bnz GoUp
    movf floor_now, W
    call below_mask_tab
    andwf req, W
    bnz GoDown
    bra MainLoop

GoUp:
    bcf LATB, DOWN_LED
    bsf LATB, UP_LED
    movlw D'1'
    movwf mv_dir
    call move_floor
    incf floor_now, F
    bra Arrived

GoDown:
    bcf LATB, UP_LED
    bsf LATB, DOWN_LED
    clrf mv_dir
    call move_floor
    decf floor_now, F

Arrived:
    bcf LATB, UP_LED
    bcf LATB, DOWN_LED
    clrf LATD
    call show_floor
    bra MainLoop
END
