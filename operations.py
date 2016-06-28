from myhdl import *

@block
def multiplier(reset, clock, enable, operand_a, operand_b, result_out):

    @always_seq(clock.posedge, reset=reset)
    def mul():
        if enable:
            result_out.next = operand_a * operand_b
            print ("%d asd1" % result_out)
    return mul

@block
def adder(reset, clock, operand_a, enable, operand_b, result_out):

    @always_seq(clock.posedge, reset=reset)
    def add():
        if enable:
            result_out.next = operand_a + operand_b
            print ("%d asd2" % result_out)
    return add

@block
def subtractor(reset, clock, enable, operand_a, operand_b, result_out):

    @always_seq(clock.posedge, reset=reset)
    def sub():
        if enable:
            result_out.next = operand_a - operand_b
            print ("%d asd3" % result_out)
    return sub

@block
def shifter(reset, clock, enable, operand_a, operand_b, result_out):

    @always_seq(clock.posedge, reset=reset)
    def sft():
        if enable:
            result_out.next = operand_a << operand_b
            print ("%d asd4" % result_out)
    return sft
