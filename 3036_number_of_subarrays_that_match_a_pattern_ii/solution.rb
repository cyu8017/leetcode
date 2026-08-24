# LeetCode 3036 - Number of Subarrays That Match a Pattern II
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

# @param {Integer[]} nums
# @param {Integer[]} pattern
# @return {Integer}
def count_matching_subarrays(nums, pattern)
  n = pattern.length
  ps = Array.new(n + 1, 0)
  ps[0] = -1
  ps[1] = 0
  p = 0
  (2..n).each do |i|
    x = pattern[i - 1]
    while p >= 0 && pattern[p] != x
      p = ps[p]
    end
    p += 1
    ps[i] = p
  end
  res = 0
  m = nums.length
  p = 0
  (1...m).each do |i|
    t = nums[i] - nums[i - 1]
    t = if t > 0
          1
        elsif t < 0
          -1
        else
          0
        end
    while p >= 0 && pattern[p] != t
      p = ps[p]
    end
    p += 1
    if p == n
      res += 1
      p = ps[p]
    end
  end
  res
end
