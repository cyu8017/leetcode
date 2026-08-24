# LeetCode 3034 - Number of Subarrays That Match a Pattern I
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

# @param {Integer[]} nums
# @param {Integer[]} pattern
# @return {Integer}
def count_matching_subarrays(nums, pattern)
  n = nums.length
  m = pattern.length
  ans = 0
  (0...n - m).each do |i|
    ok = 1
    k = 0
    while k < m && ok != 0
      ok = 0 if f_rel(nums[i + k], nums[i + k + 1]) != pattern[k]
      k += 1
    end
    ans += ok
  end
  ans
end

def f_rel(a, b)
  return 0 if a == b

  a < b ? 1 : -1
end
