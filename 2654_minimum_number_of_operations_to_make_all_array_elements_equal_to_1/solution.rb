# LeetCode 2654 - Minimum Number of Operations to Make All Array Elements Equal to 1
# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end
  n = nums.length
  ones = nums.count(1)
  return n - ones if ones > 0

  best = n + 1
  n.times do |i|
    g = 0
    (i...n).each do |j|
      g = gcd.call(g, nums[j])
      if g == 1
        best = [best, j - i].min
        break
      end
    end
  end
  return -1 if best == n + 1

  best + n - 1
end
