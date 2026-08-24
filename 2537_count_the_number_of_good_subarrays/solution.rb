# LeetCode 2537 - Count the Number of Good Subarrays
# https://leetcode.com/problems/count-the-number-of-good-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_good(nums, k)
  freq = Hash.new(0)
  pairs = 0
  ans = 0
  left = 0
  nums.each_with_index do |x, right|
    pairs += freq[x]
    freq[x] += 1
    while pairs >= k
      ans += nums.length - right
      freq[nums[left]] -= 1
      pairs -= freq[nums[left]]
      left += 1
    end
  end
  ans
end
