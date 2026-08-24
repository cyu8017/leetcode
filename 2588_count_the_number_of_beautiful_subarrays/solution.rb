# LeetCode 2588 - Count the Number of Beautiful Subarrays
# https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def beautiful_subarrays(nums)
  freq = Hash.new(0)
  freq[0] = 1
  xorv = 0
  ans = 0
  nums.each do |x|
    xorv ^= x
    ans += freq[xorv]
    freq[xorv] += 1
  end
  ans
end
