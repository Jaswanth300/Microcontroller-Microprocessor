/* ==============================================================================
 * Experiment 18: Design and Simulation of Multi-Floor Elevator Controller
 * Target Microcontroller: Microchip PIC18F45K22
 * Compiler: MPLAB XC8 C Compiler
 * Author: Naga Jaswanth (Reg. No: 192424300)
 * ==============================================================================
 */

#include <xc.h>
#include <stdint.h>

#define _XTAL_FREQ 16000000UL

#pragma config FOSC = INTIO67
#pragma config PLLCFG = OFF
#pragma config WDTEN = OFF
#pragma config LVP = OFF
#pragma config MCLRE = EXTMCLR
#pragma config PBADEN = OFF

#define FLOORS 4
#define STEPS_PER_FLOOR 200
#define STEP_DELAY 10
#define DOOR_TIME 2000

#define IDLE 0
#define UP 1
#define DOWN 2
#define DOOR 3

const unsigned char seg[4] = { 0x3F, 0x06, 0x5B, 0x4F };       // 7-segment 0, 1, 2, 3
const unsigned char motor[4] = { 0x09, 0x0C, 0x06, 0x03 };     // Stepper 4-phase sequence

volatile unsigned char tick = 0;
unsigned char request = 0;
unsigned char floor = 0;
unsigned char state = IDLE;
unsigned char direction = UP;
unsigned char phase = 0;
unsigned char old_buttons = 0;
unsigned int steps = 0;
unsigned int timer = 0;

void display(void) {
    LATC = seg[floor];
    LATAbits.LATA0 = (state == UP);
    LATAbits.LATA1 = (state == DOWN);
    LATAbits.LATA2 = (state == DOOR);
    if (state != UP && state != DOWN)
        LATD = 0;
}

unsigned char above(void) {
    unsigned char mask = (unsigned char)(0x0F & ~((1 << (floor + 1)) - 1));
    return request & mask;
}

unsigned char below(void) {
    unsigned char mask = (1 << floor) - 1;
    return request & mask;
}

void decide(void) {
    if (request & (1 << floor)) {
        request &= ~(1 << floor);
        state = DOOR;
        timer = DOOR_TIME;
    } else if (direction == UP && above()) {
        state = UP;
        timer = STEP_DELAY;
    } else if (direction == DOWN && below()) {
        state = DOWN;
        timer = STEP_DELAY;
    } else if (above()) {
        direction = UP;
        state = UP;
        timer = STEP_DELAY;
    } else if (below()) {
        direction = DOWN;
        state = DOWN;
        timer = STEP_DELAY;
    } else {
        state = IDLE;
        timer = 0;
    }
    steps = 0;
    display();
}

void elevator(void) {
    unsigned char buttons = (~PORTB) & 0x0F;
    unsigned char new_buttons = buttons & ~old_buttons;
    request |= new_buttons;
    old_buttons = buttons;

    switch (state) {
        case IDLE:
            if (request != 0) decide();
            break;
        case DOOR:
            if (timer > 0) timer--;
            if (timer == 0) decide();
            break;
        case UP:
        case DOWN:
            if (timer > 0) timer--;
            if (timer == 0) {
                timer = STEP_DELAY;
                if (state == UP) {
                    phase = (phase + 1) & 0x03;
                } else {
                    phase = (phase + 3) & 0x03;
                }
                LATD = motor[phase];
                steps++;
                if (steps >= STEPS_PER_FLOOR) {
                    if (state == UP) floor++;
                    else floor--;
                    decide();
                }
            }
            break;
    }
}

void main(void) {
    OSCCON = 0x72;      // 16 MHz internal oscillator
    ANSELA = 0;
    ANSELB = 0;
    ANSELC = 0;
    ANSELD = 0;

    TRISA = 0x00;       // Status LEDs output
    TRISB = 0x0F;       // Floor buttons input
    WPUB = 0x0F;        // Weak pull-ups enabled
    TRISC = 0x00;       // 7-segment display output
    TRISD = 0x00;       // Stepper motor driver output

    display();
    while (1) {
        elevator();
        __delay_ms(1);
    }
}
