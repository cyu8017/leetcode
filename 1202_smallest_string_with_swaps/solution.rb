# LeetCode 1202 - Smallest String with Swaps
# https://leetcode.com/problems/smallest-string-with-swaps/

# @param {String} s
# @param {Integer[][]} pairs
# @return {String}
def smallest_string_with_swaps(s, pairs)
  parent = (0...s.length).to_a
  find = lambda do |x|
    while x != parent[x]
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  pairs.each do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb
  end
  groups = Hash.new { |h, k| h[k] = [] }
  s.each_char.with_index { |ch, i| groups[find.call(i)] << ch }
  groups.each_value { |chars| chars.sort!.reverse! }
  (0...s.length).map { |i| groups[find.call(i)].pop }.join
end
