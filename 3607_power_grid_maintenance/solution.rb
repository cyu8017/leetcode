# LeetCode 3607 - Power Grid Maintenance
# https://leetcode.com/problems/power-grid-maintenance/

# @param {Integer} c
# @param {Integer[][]} connections
# @param {Integer[][]} queries
# @return {Integer[]}
def process_queries(c, connections, queries)
  parent = (0..c).to_a
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb
    if ra < rb
      parent[rb] = ra
    else
      parent[ra] = rb
    end
  end
  connections.each { |e| unite.call(e[0], e[1]) }
  online = Array.new(c + 1, true)
  comp = {}
  (1..c).each do |i|
    r = find.call(i)
    (comp[r] ||= []) << i
  end
  comp.each_value(&:sort!)
  ptr = {}
  ans = []
  queries.each do |q|
    t, x = q[0], q[1]
    if t == 2
      online[x] = false
      next
    end
    if online[x]
      ans << x
      next
    end
    r = find.call(x)
    ids = comp[r]
    p = ptr[r] || 0
    p += 1 while p < ids.length && !online[ids[p]]
    ptr[r] = p
    ans << (p < ids.length ? ids[p] : -1)
  end
  ans
end
