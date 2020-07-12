def tower_of_hanoi(n, src, dst, aux):
    if n > 0:
        tower_of_hanoi(n - 1, src, aux, dst)  # moves top n-1 disks to aux

        print("Move disk", n, "from", src, "to", dst)  # moves last disk to dst

        tower_of_hanoi(n - 1, aux, dst, src)  # moves top n-1 disk to dst


n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
