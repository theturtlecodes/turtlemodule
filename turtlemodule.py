def strlength(x):
  xArray = list(str(x))
  return len(xArray)

def intlength(x):
  x = round(x)
  xArray = list(str(int(x)))
  return len(xArray)
  
def commatise(x, y = ','):
  if x >= 1e+16:
    return str(x)
  nlength = intlength(x)
  xlist = list(str(x))
  if y == '.':
    try:
      xlist[xlist.index('.')] = ','
    except ValueError:
      pass
  camount = nlength // 3
  if '-' in xlist:
    nlength -= 1
  if nlength % 3 == 0:
    if nlength != 3:
      camount -= 1
      while camount > 0:
        xlist.insert(camount * 3, y)
        camount -= 1
  if nlength % 3 == 1:
    while camount > 0:
        xlist.insert(camount * 3 - 2, y)
        camount -= 1
  if nlength % 3 == 2:
    while camount > 0:
      xlist.insert(camount * 3 - 1, y)
      camount -= 1
  return ''.join(xlist)
  
def uncommatise(x, y = [','], z = False):
  nonintlocs = []
  xlist = list(x)
  k = 0
  while k < len(xlist):
    if not xlist[k].isdigit() and xlist[k] in y:
      del xlist[k]
    else:
      k += 1
  ucint = ''.join(xlist)
  if z:
    return float(ucint)
  else:
    return ucint
def charranking(x, y = [' ', ',', '.']):
  charstodate = []
  for z in x:
    z = z.lower()
    found = False
    for item in charstodate:
      if item[0] == z:
        item[1] += 1
        found = True
        break
    if not found and z not in y:
      charstodate.append([z, 1])
  return sorted(charstodate, key = lambda x: x[1], reverse = True)
