def convert2D(filename):
    # File opening 
    f0 = open("temp.mesh", "r")
    f = open("mesh/" + filename + ".mesh", "w")

    # File conversion 
    for line in f0:
        f.write(line) # default : copy line
        
        if "Dimension" in line: # Change dimension to 2
            f.write(" 2\n")
            f0.readline()
        
        elif "Vertices" in line: # Remove z-coordinate from vertices
            nb = int(f0.readline())
            f.write(f" {nb}\n")
            
            i=0
            while(i<nb):
                l = f0.readline().split()
                tmp = ' '*(21-len(l[0])) + l[0] + ' '*(26-len(l[1])) + l[1] + ' '*6 + l[3] + '\n'
                f.write(tmp)
                i+=1

    # File closing
    f0.close()
    f.close()