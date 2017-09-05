count_steps = 0

def TowerOfHanoi(disk_Nos, frm, to, using):
    if disk_Nos is 1:
        global count_steps
        count_steps += 1
        print("%d. Move disk from tower %s to tower %s" % (count_steps, frm, to))

    else:
        TowerOfHanoi(disk_Nos - 1, frm, to, using)
        TowerOfHanoi(1, frm, using, to)
        TowerOfHanoi(disk_Nos - 1, using, frm, to)


TowerOfHanoi(5, 'A', 'B', 'C')
    
