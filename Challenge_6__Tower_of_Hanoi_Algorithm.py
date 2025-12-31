def toh(no_of_disk : int, from_rod, to_rod, aux_rod):
    if no_of_disk <= 1:
        print(f"Disk {no_of_disk} moved from {from_rod} to {to_rod}")
        return
        
    toh(no_of_disk - 1, from_rod, aux_rod, to_rod)
    
    print(f"Disk {no_of_disk} moved from {from_rod} to {to_rod}")
    
    toh(no_of_disk - 1, aux_rod, to_rod, from_rod)

#toh(3,'A','C','B')
