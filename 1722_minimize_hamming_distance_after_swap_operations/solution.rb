# LeetCode 1722 - Minimize Hamming Distance After Swap Operations
# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

# @param {Integer[]} source
# @param {Integer[]} target
# @param {Integer[][]} allowed_swaps
# @return {Integer}
def minimum_hamming_distance(source, target, allowed_swaps)
  n = source.length
  parent = (0...n).to_a
  find = lambda do |x|
    while parent[x] != x
      parent[x] = parent[parent[x]]
      x = parent[x]
    end
    x
  end
  union = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[rb] = ra if ra != rb
  end

  allowed_swaps.each { |a, b| union.call(a, b) }
  groups = Hash.new { |hash, key| hash[key] = Hash.new(0) }
  source.each_with_index { |value, i| groups[find.call(i)][value] += 1 }
  ans = 0
  target.each_with_index do |value, i|
    group = groups[find.call(i)]
    if group[value] > 0
      group[value] -= 1
    else
      ans += 1
    end
  end
  ans
end
