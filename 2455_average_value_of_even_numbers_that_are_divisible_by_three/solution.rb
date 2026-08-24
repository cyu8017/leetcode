# LeetCode 2455 - Average Value of Even Numbers That Are Divisible by Three
# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

# @param {Integer[]} nums
# @return {Integer}
def average_value(nums)
  total = 0
  cnt = 0
  nums.each do |x|
    if x % 6 == 0
      total += x
      cnt += 1
    end
  end
  cnt == 0 ? 0 : total / cnt
end
