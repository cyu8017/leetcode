# LeetCode 4011 - Count Subarrays With Even Odd Ratio I
# https://leetcode.com/problems/count-subarrays-with-even-odd-ratio-i/

# @param {Integer[]} nums
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def count_ratio_subarrays(nums, a, b)
  n = nums.length
  ans = 0
  n.times do |i|
    y = 0
    (i...n).each do |j|
      y += nums[j] % 2
      x = j - i + 1 - y
      ans += 1 if y > 0 && x * b <= y * a
    end
  end
  ans
end
