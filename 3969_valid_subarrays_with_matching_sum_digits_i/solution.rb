# LeetCode 3969 - Valid Subarrays With Matching Sum Digits I
# https://leetcode.com/problems/valid-subarrays-with-matching-sum-digits-i/

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def count_valid_subarrays(nums, x)
  n = nums.length
  ans = 0
  n.times do |l|
    s = 0
    (l...n).each do |r|
      s += nums[r]
      if s % 10 == x
        t = s.to_s
        ans += 1 if t[0].ord - 48 == x
      end
    end
  end
  ans
end
