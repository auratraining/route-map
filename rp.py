def get_route_map(fname):
	rfd=open(fname,'r')
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
					print (r, c, rmap[r][c])
					map_table['Entrance'].append((r,c)) 
				
def populate_edges(rmap, map_table):
	for r, line in enumerate(rmap):
		for c, cell in enumerate(line):
				if (rmap[r][c] == 'R'):
					if( (rmap[r-1][c]=='R' and rmap[r][c+1]=='R') or
						(rmap[r][c+1]=='R' and rmap[r+1][c]=='R') or
						(rmap[r][c-1]=='R' and rmap[r+1][c]=='R') or
						(rmap[r-1][c]=='R' and rmap[r][c-1]=='R')):
							
						print (r, c, rmap[r][c])
						map_table['Edge'].append((r,c)) 
							

			
			


		
def main():
	map_table = {
		"Entrance" : [],
		"Edge" : []
	}
	filename = "s.txt"
	route_map = get_route_map(filename)
	#print (route_map)
	
	populate_entrance(route_map, map_table)
	print (map_table)
	
	populate_edges(route_map, map_table)
	print (map_table)  

if (__name__ == "__main__"):
	main()