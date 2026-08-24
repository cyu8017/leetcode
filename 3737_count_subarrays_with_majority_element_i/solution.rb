# LeetCode 3737 - Count Subarrays With Majority Element I
# https://leetcode.com/problems/count-subarrays-with-majority-element-i/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def count_majority_subarrays(nums, target)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    cnt = 0
    (i...n).each do |j|
      cnt += 1 if nums[j] == target
      ans += 1 if cnt * 2 > j - i + 1
    end
  end
  ans
end
