# LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

# @param {Integer[]} nums
# @return {Integer}
def find_max_k(nums)
  seen = {}
  ans = -1
  nums.each do |x|
    seen[x] = true
    if x > 0 && seen[-x] && x > ans
      ans = x
    elsif x < 0 && seen[-x] && -x > ans
      ans = -x
    end
  end
  ans
end
