def first_fit(partitions, processes):
    print('\nFirst-fit')
    i = 0
    MustWait = None
    while i < len(processes):
        complete = [True]*len(processes)
        for j in range(len(partitions)):
            if i < len(processes):
                if processes[i] <= partitions[j]:
                    print(f"{processes[i]}K is put in {
                          partitions[j]}K partition")
                    partitions[j] -= processes[i]
                    complete[i] = False
                    i += 1
                else:
                    MustWait = processes[i]
        if all(complete):
            print(f'{MustWait}K must wait')
            i += 1


def best_fit(partitions, processes):
    print('\nBest-fit')
    MustWait = None
    for i in range(len(processes)):
        partitions.sort()
        complete = [True]*len(processes)
        for j in range(len(partitions)):
            if i < len(processes):
                if processes[i] <= partitions[j]:
                    print(f"{processes[i]}K is put in {
                          partitions[j]}K partition")
                    partitions[j] -= processes[i]
                    complete[i] = False
                    break
                else:
                    MustWait = processes[i]
        if all(complete):
            print(f'{MustWait}K must wait')


def worst_fit(partitions, processes):
    print('\nWorst-fit')
    MustWait = None
    for i in range(len(processes)):
        partitions.sort()
        partitions.reverse()
        complete = [True]*len(processes)
        for j in range(len(partitions)):
            if i < len(processes):
                if processes[i] <= partitions[j]:
                    print(f"{processes[i]}K is put in {
                          partitions[j]}K partition")
                    partitions[j] -= processes[i]
                    complete[i] = False
                    break
                else:
                    MustWait = processes[i]
        if all(complete):
            print(f'{MustWait}K must wait')


first_fit([100, 500,  200, 300, 600], [212, 417, 112, 426])

best_fit([100, 500,  200, 300, 600], [212, 417, 112, 426])

worst_fit([100, 500,  200, 300, 600], [212, 417, 112, 426])
