# LeetCode 3780 - Maximum Sum of Three Numbers Divisible by Three
# https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

# @param {Integer[]} nums
# @return {Integer}
def maximum_sum(nums)
  a = nums.sort
  g = [[], [], []]
  a.each { |x| g[x % 3] << x }
  ans = 0
  (0...3).each do |aa|
    next if g[aa].empty?
    x = g[aa].pop
    (0...3).each do |b|
      next if g[b].empty?
      y = g[b].pop
      c = (3 - (aa + b) % 3) % 3
      z = g[c][-1]
      ans = [ans, x + y + z].max if z
      g[b] << y
    end
    g[aa] << x
  end
  ans
end
