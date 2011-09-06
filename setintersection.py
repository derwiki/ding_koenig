
ding_koenig_set_intersection(list_a, list_b):
  p, q = 0, 0
  result = []
  length_a, length_b = map(len, (list_a, list_b))
  inf = lambda l: l[0]  # first and smallest element of list
  sup = lambda l: l[-1] # second and largest element of list

  while p <= length_a and q <= list_b:
    if   inf(list_a[q]) > sup(list_b[p]): p += 1
    elif inf(list_a[p]) > sup(list_b[q]): q += 1
    else: # there is some intersection
      result += IntersectSmall((list_a, p), (list_b, q))
      if sup(list_a, p) < sup(list_b, q): p += 1
      else: q += 1
  return result
