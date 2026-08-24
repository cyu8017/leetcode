# LeetCode 3101 - Count Alternating Subarrays
# https://leetcode.com/problems/count-alternating-subarrays/

# @param {Integer[]} nums
# @return {Integer}
def count_alternating_subarrays(nums)
  ans = 1
  s = 1
  (1...nums.length).each do |i|
    if nums[i] != nums[i - 1]
      s += 1
    else
      s = 1
    end
    ans += s
  end
  ans
end
