# LeetCode 1569 - Number of Ways to Reorder Array to Get Same BST
# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

# @param {Integer[]} nums
# @return {Integer}
def num_of_ways(nums)
  mod = 1_000_000_007
  n = nums.length
  choose = Array.new(n + 1) { Array.new(n + 1, 0) }
  (0..n).each do |i|
    choose[i][0] = choose[i][i] = 1
    (1...i).each { |j| choose[i][j] = (choose[i - 1][j - 1] + choose[i - 1][j]) % mod }
  end
  ways = lambda do |values|
    return 1 if values.length < 3
    left = values[1..].select { |x| x < values[0] }
    right = values[1..].select { |x| x > values[0] }
    choose[values.length - 1][left.length] * ways.call(left) * ways.call(right) % mod
  end
  (ways.call(nums) - 1) % mod
end
