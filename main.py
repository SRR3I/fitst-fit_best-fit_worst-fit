def first_fit(partitions, processes):
    i = 0
    MustWait = None
    while i < len(processes):
        complete = [True]*len(processes)
        for j in range(len(partitions)):
            if i < len(processes):
                if processes[i] <= partitions[j]:
                    print(f"{processes[i]} is put in {partitions[j]}")
                    partitions[j] -= processes[i]
                    complete[i] = False
                    i += 1
                else:
                    MustWait = processes[i]
        if all(complete):
            print(MustWait, 'must want')
            break


def best_fit(partitions, processes):
    return


def worst_fit(partitions, processes):
    return


f = first_fit([100, 500,  200, 300, 600], [212, 417, 112, 426])
