# LeetCode 1319 - Number Of Operations To Make Network Connected
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

def make_connected(n, connections)
  return -1 if connections.length < n - 1
  parent = (0...n).to_a
  find = lambda do |x|
    while x != parent[x]
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  connections.each do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb if ra != rb
  end
  (0...n).map { |i| find.call(i) }.uniq.length - 1
end
