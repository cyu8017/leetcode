# LeetCode 2932 - Maximum Strong Pair XOR I
# https://leetcode.com/problems/maximum-strong-pair-xor-i/

# @param {Integer[]} nums
# @return {Integer}
def maximum_strong_pair_xor(nums)
  ans = 0
  (0...nums.length).each do |i|
    (i...nums.length).each do |j|
      x = nums[i]
      y = nums[j]
      if (x - y).abs <= [x, y].min
        xorr = x ^ y
        ans = xorr if xorr > ans
      end
    end
  end
  ans
end
