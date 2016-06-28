from myhdl import *
from operations import *

def mul(c, a, b):
    c.next = a * b

def add(c, a, b):
    c.next = a + b

def sub(c, a, b):
    c.next = a - b

def shift_l(c, a, b):
    c.next = a << b

@block
def controlunit(reset, clock, operand, result):
    
    # signal declarations
    sel = Signal(intbv(0)[2:])
    opa = Signal(intbv(0)[4:])
    opb = Signal(intbv(0)[4:])

    # transfer instruction into registers
    @always_comb
    def assign():
        # select operation
        sel.next = operand[10:8]

        # select operand A
        opa.next = operand[8:4]

        # select operand B
        opb.next = operand[4:0]

    # control unit (FSM) used to decide which operation to perform
    @always_seq(clock.posedge, reset = reset)
    def assign2():

        if sel == 0:
            # multiply opA and opB
            mul(result, opa, opb)

        elif sel == 1:
            # add opA and opB
            add(result, opa, opb)


        elif sel == 2:
            # sub opA and opB
            sub(result, opa, opb)

        elif sel == 3:
            # shift_l opA and opB
            shift_l(result, opa, opb)

        else:
            pass

    return assign, assign2

def convert():

    clock = Signal(bool(0))
    reset = ResetSignal(0, active=True, async=True)

    operand = Signal(intbv(0)[10:])
    result = Signal(intbv(0)[10:])

    inst = controlunit(reset, clock, operand, result)
    inst.convert(hdl='VHDL')


if __name__ == '__main__':
    convert()