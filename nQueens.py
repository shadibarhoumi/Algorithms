def n_queens(c, n, coords):
  # global counter for solutions
  global solutions
  for spot in range(n):
    # test each spot in this column to see if it works
    if is_valid(c, spot, coords):
      # if we've found a viable spot in this column,
      # add this spot to the current working solution 
      coords.append([c, spot])
      if c == n-1:
        # if we've found a viable spot and we're
        # at the end, we've won!
        solutions += 1
        # inc sols and pop coord, try next space
        coords.pop()
      else:
        # if we're not at the last column, check if
        # there is a viable spot in the next column
        if not n_queens(c+1, n, coords):
          # if there isn't a viable spot in the next column, the mistake
          # was in this column (or previous), so pop coordinates and try
          # another spot
          coords.pop()
  return False


def is_valid(x, y, coords):
  for coord in coords:
    # if candidate is a square dist away, in same col, or same row, return false
    if (abs(coord[0] - x) == abs(coord[1] - y)) or (x == coord[0]) or (y == coord[1]):
      return False
  return True




solutions = 0
n = 8
n_queens(0, n, [])
print "total solutions for n = %d: %d" % (n, solutions)