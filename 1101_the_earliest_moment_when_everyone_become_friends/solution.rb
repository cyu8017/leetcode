# LeetCode 1101 - The Earliest Moment When Everyone Become Friends
# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

# @param {Integer[][]} logs
# @param {Integer} n
# @return {Integer}
def earliest_acq(logs, n)
  parent = (0...n).to_a
  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  logs = logs.sort_by { |t, _, _| t }
  components = n
  logs.each do |t, a, b|
    ra = find.call(a)
    rb = find.call(b)
    next if ra == rb
    parent[rb] = ra
    components -= 1
    return t if components == 1
  end
  -1
end
