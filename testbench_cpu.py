from myhdl import *
from controlunit import *
from operations import *
from clock import *

def test_divider():


    clock = Signal(bool(0))
    reset = ResetSignal(0, active=True, async=True)

    operand = Signal(intbv(0)[10:])
    result = Signal(intbv(0)[10:])

    @block
    def bench_divider():
        # instantiation of controlunit
        inst = controlunit(reset, clock, operand, result)
        # instatiation of clock
        inst_clock = tbclock(clock)

        @instance
        def tbstim():

            reset.next = True
            yield delay(40)
            yield clock.posedge
            reset.next = False

            # operation = 00(mul) opA = 2 opB = 15            
            operand.next = 47
            yield clock.posedge
            yield clock.posedge
            print ("%d" %result)

            # operation = 01(add)
            operand.next = 289  
            yield clock.posedge
            yield clock.posedge
            print ("%d" %result)

            #operation = 10(sub)
            operand.next = 545
            yield clock.posedge
            yield clock.posedge
            print ("%d" %result)

            #operation = 11(shifter(left))
            operand.next = 801
            yield clock.posedge
            yield clock.posedge
            print ("%d" %result)

            raise StopSimulation

        return tbstim, inst, inst_clock

    inst1 = bench_divider()
    inst1.config_sim(trace=False)
    inst1.run_sim()
    bench_divider().convert(hdl='VHDL')

test_divider()