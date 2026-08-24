# LeetCode 2799 - Count Complete Subarrays in an Array
# https://leetcode.com/problems/count-complete-subarrays-in-an-array/

# @param {Integer[]} nums
# @return {Integer}
def count_complete_subarrays(nums)
  need = nums.uniq.length
  ans = 0
  n = nums.length
  (0...n).each do |i|
    seen = {}
    (i...n).each do |j|
      seen[nums[j]] = true
      if seen.length == need
        ans += n - j
        break
      end
    end
  end
  ans
end
