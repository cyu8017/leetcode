# LeetCode 3937 - Minimum Operations To Make Array Modulo Alternating I
# https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  vals = nums.map { |v| v % k }
  ans = 2_147_483_647
  k.times do |x|
    k.times do |y|
      next if x == y
      cnt = 0
      vals.each_with_index do |v, i|
        target = (i & 1) != 0 ? y : x
        diff = (target - v).abs
        cnt += [diff, k - diff].min
      end
      ans = cnt if cnt < ans
    end
  end
  ans
end
