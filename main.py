def first_fit(partitions, processes):
    print('\nFirst-fit')
    i = 0
    MustWait = None
    while i < len(processes):
        complete = [True]*len(processes)
        for j in range(len(partitions)):
            if i < len(processes):
                if processes[i] <= partitions[j]:
                    print(f"{processes[i]} is put in {partitions[j]} partition")
                    partitions[j] -= processes[i]
                    complete[i] = False
                    i += 1
                else:
                    MustWait = processes[i]
        if all(complete):
            print(MustWait, 'must wait')
            break

def best_fit(partitions, processes):
    print('\nBest-fit')
    MustWait = None
    for i in range(len(processes)):
        partitions.sort()
        complete = [True]*len(processes)
        for j in range(len(partitions)):
            if i < len(processes):
                if processes[i] <= partitions[j]:
                    print(f"{processes[i]} is put in {partitions[j]} partition")
                    partitions[j] -= processes[i]
                    complete[i] = False
                    break
                else:
                    MustWait = processes[i]
        if MustWait != None and all(complete):
            print(MustWait, 'must wait')


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
                    print(f"{processes[i]} is put in {partitions[j]} partition")
                    partitions[j] -= processes[i]
                    complete[i] = False
                    break
                else:
                    MustWait = processes[i]
        if MustWait != None and all(complete):
            print(MustWait, 'must wait')


partition = [100, 500,  200, 300, 600]
process = [212, 417, 112, 426]
first_fit(partition, process)


partition = [100, 500,  200, 300, 600]
process = [212, 417, 112, 426]
best_fit(partition, process)


partition = [100, 500,  200, 300, 600]
process = [212, 417, 112, 426]
worst_fit(partition, process)
