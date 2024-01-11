# Cube finder
def cube_finder(m):
    cubes={}
    for i in range(1,m+1):
        cubes[i]=i**3
    return cubes
print(cube_finder(10))
