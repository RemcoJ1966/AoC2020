from typing import Generator, List, Tuple


def read_input() -> Generator[str, None, None]:
    with open('input', 'r') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()

def nop(prog_ctr: int, accu: int):
    return prog_ctr + 1, accu

def jmp(param: int, prog_ctr: int, accu: int):
    return prog_ctr + param, accu

def acc(param: int, prog_ctr: int, accu: int):
    return prog_ctr + 1, accu + param

def run(boot_code: List[Tuple[str, int]], flip_pc: int) -> Tuple[bool, int]:
    accu = 0
    prog_ctr = 0
    while True:
        if prog_ctr >= len(boot_code):
            return True, accu

        instr = flip_instr(boot_code[prog_ctr][0], prog_ctr, flip_pc)
        param = boot_code[prog_ctr][1]
        boot_code[prog_ctr] = ('', 0)
        if 'nop' == instr:
            prog_ctr, accu = nop(prog_ctr, accu)
        if 'jmp' == instr:
            prog_ctr, accu = jmp(param, prog_ctr, accu)
        if 'acc' == instr:
            prog_ctr, accu = acc(param, prog_ctr, accu)
        if '' == instr:
            return False, accu

def flip_instr(instr: str, prog_ctr: int, flip_pc: int) -> str:
    if (-1 == flip_pc or prog_ctr != flip_pc):
        return instr

    if 'nop' == instr:
        return 'jmp'
    if 'jmp' == instr:
        return 'nop'
    return instr
    

if __name__ == '__main__':

    boot_code_orig = []
    for line in read_input():
        operand = int(line[5:])
        boot_code_orig.append((line[:3], operand if '+' == line[4] else -operand))

    boot_code = boot_code_orig.copy()
    terminated, accu = run(boot_code, -1)
    print(f'The value in the accumulator is {accu}')

    max_prog_ctr = len(boot_code)
    for flip_pc in list(range(max_prog_ctr)):
        boot_code = boot_code_orig.copy()
        terminated, accu = run(boot_code, flip_pc)
        if terminated:
            print(f'The value in the accumulator is {accu}')
            break
