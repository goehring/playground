#Just a little formalization of the training plan, 2026/07/21

slow = 10
fast = 16
xxfast = 18
accel = 20


def run(dist, pace):
    print("running", dist, " m with pace ", pace, " km/h")

def brk(time):
    print("break for ", time, " seconds")

#training starts here:
run(3700, slow)
run(400, accel)

for n in range(4):
    run(400, fast)
    brk(60)
    run((n+2)*400, fast)

    if n>0:
        run(400, slow)
    else:
        brk(60)

run(400, xxfast)
run(1600, slow)
