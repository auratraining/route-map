def get_route_map(fname):
    rfd = open(fname, 'r')
    ldata = []
    while(1):
        data = rfd.readline()
        #print (data)
        if (len(data) <= 0):
            break
        x = data.strip().split("\t")
        ldata.append(x)

    return ldata


def populate_entrance(rmap, map_table):
    for r, line in enumerate(rmap):
        for c, cell in enumerate(line):
            if (rmap[r][c] == 'E'):
                #print (r, c, rmap[r][c])
                map_table['Entrance'].append((r, c))


def populate_edges(rmap, map_table):
    for r, line in enumerate(rmap):
        for c, cell in enumerate(line):
            if (rmap[r][c] == 'R'):
                if((rmap[r-1][c] == 'R' and rmap[r][c+1] == 'R') or
                        (rmap[r][c+1] == 'R' and rmap[r+1][c] == 'R') or
                        (rmap[r][c-1] == 'R' and rmap[r+1][c] == 'R') or
                        (rmap[r-1][c] == 'R' and rmap[r][c-1] == 'R')):

                    #print (r, c, rmap[r][c])
                    map_table['Edge'].append((r, c))

def is_valid_cell(rmap, map_table, r, c):
    if (rmap[r][c] == 'w' or rmap[r][c] == 'E'):
        return False

    return True
    
def is_edge(rmap, map_table, r, c):
    if (rmap[r][c] == 'R' and (r, c) in map_table["Edge"]):
        return True
    return False

def top_neighbour(rmap, map_table, r, c):
    i = 0
    r = r - 1 ; c = c
    while(True):
        if (is_valid_cell(rmap, map_table, r, c) == False):
            break

        if (is_edge(rmap, map_table, r, c) == True):
            print ((r, c), end=", ")
            return (r, c)
        r = r - 1

def right_neighbour(rmap, map_table, r, c):
    i = 0
    r = r; c = c + 1
    while(True):
        if (is_valid_cell(rmap, map_table, r, c) == False):
            break

        if (is_edge(rmap, map_table, r, c) == True):
            print ((r, c), end=", ")
            return (r, c)
        c = c + 1

def bottom_neighbour(rmap, map_table, r, c):
    i = 0
    r = r + 1; c = c
    while(True):
        if (is_valid_cell(rmap, map_table, r, c) == False):
            break

        if (is_edge(rmap, map_table, r, c) == True):
            print ((r, c), end=", ")
            return (r, c)
        r = r + 1

def left_neighbour(rmap, map_table, r, c):
    i = 0
    r = r; c = c - 1
    while(True):
        if (is_valid_cell(rmap, map_table, r, c) == False):
            break

        if (is_edge(rmap, map_table, r, c) == True):
            print ((r, c), end=", ")
            return (r, c)
        c = c - 1

def populate_neighbour_edges(rmap, map_table):
    print(f'-->{map_table["Edge"]}')
    for i, edge in enumerate(map_table["Edge"]):
        print (f"-->{edge}  :", end="")
        r, c = edge
        top_neighbour(rmap, map_table, r, c)
        right_neighbour(rmap, map_table, r, c)
        bottom_neighbour(rmap, map_table, r, c)
        left_neighbour(rmap, map_table, r, c)
        print ()

    return

def main():
    map_table = {
        "Entrance": [],
        "Edge": [],
        "Neighbouredges": []
    }
    filename = "s.txt"
    route_map = get_route_map(filename)
    #print (route_map)

    populate_entrance(route_map, map_table)
    #print (map_table)

    populate_edges(route_map, map_table)
    #print(map_table)

    populate_neighbour_edges(route_map, map_table)
    #print(map_table["Edge"])


if (__name__ == "__main__"):
    main()
