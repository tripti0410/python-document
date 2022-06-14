# taking input
n=int(input('Enter n: '))
package=[]
packagespre={}
for i in range(0,n):
  pack=input("package: ")
  dep=input("dependency: ")
  package.append([pack,dep])
  if pack in packagespre:
    packagespre[pack].append(dep)
  else:
    packagespre[pack]=[dep]
  if dep in packagespre:
    packagespre[dep].append(pack)
  else:
    packagespre[dep]=[]

result=[]
visited, cycle=set(), set()
def dfs(crs):
  if crs in cycle:
      return False
  if crs in visited:
      return True
  cycle.add(crs)
  for pre in packagespre[crs]:
      if dfs(pre)== False:
          return False
  cycle.remove(crs)
  visited.add(crs)
  result.append(crs)
  return True

check=True
for c in range(len(package)):
  for d in range(len(package[c])):
    if dfs(package[c][d])== False:
      print("Package can't be installed.")
      check=False
      break
if check:
  print(result)
