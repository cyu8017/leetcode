# LeetCode 1955 - Count Number of Special Subsequences
# https://leetcode.com/problems/count-number-of-special-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def count_special_subsequences(nums)
  mod = 10**9 + 7
  a = b = c = 0
  nums.each do |x|
    if x.zero?
      a = (a * 2 + 1) % mod
    elsif x == 1
      b = (b * 2 + a) % mod
    else
      c = (c * 2 + b) % mod
    end
  end
  c
end
