def toh(no_of_disk : int, from_rod, to_rod, aux_rod):
    if no_of_disk == 1:
        print(f"Move {from_rod} to {to_rod}")
        return
    toh(no_of_disk - 1, from_rod, aux_rod, to_rod)
    toh(1, from_rod, to_rod, aux_rod)
    toh(no_of_disk - 1, aux_rod, to_rod, from_rod)


