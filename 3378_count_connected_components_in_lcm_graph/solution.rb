# LeetCode 3378 - Count Connected Components in LCM Graph
# https://leetcode.com/problems/count-connected-components-in-lcm-graph/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def gcd_int(a, b)
  while b != 0
    a, b = b, a % b
  end
  a
end

# @param {Integer[]} nums
# @param {Integer} threshold
# @return {Integer}
def count_components(nums, threshold)
  n = nums.length
  parent = n.times.to_a
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    parent[ra] = rb if ra != rb
  end
  idx = {}
  nums.each_with_index { |v, i| idx[v] = i }
  (1..threshold).each do |d|
    first = -1
    m = d
    while m <= threshold
      if idx.key?(m)
        i = idx[m]
        if first == -1
          first = i
        elsif nums[first] * nums[i] / gcd_int(nums[first], nums[i]) <= threshold
          unite.call(first, i)
        end
      end
      m += d
    end
  end
  n.times do |i|
    ((i + 1)...n).each do |j|
      a = nums[i]
      b = nums[j]
      g = gcd_int(a, b)
      unite.call(i, j) if (a / g) * b <= threshold
    end
  end
  n.times.map { |i| find.call(i) }.uniq.length
end
