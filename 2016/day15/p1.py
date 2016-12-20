def get_disc(line):
    spl = line.split()
    return int(spl[3]), int(spl[-1][:-1])

def can_pass(t, discs):
    for c in xrange(len(discs)):
        sz, ini = discs[c]
        if (ini + t+c+1) % sz != 0:
            return False
    return True

def solve(lines):
    discs = map(get_disc, lines)
    t = 0
    while not can_pass(t, discs):
        t += 1
    return t

fname = 'input.txt'
lines = [line.strip() for line in open(fname).readlines()]
print solve(lines)