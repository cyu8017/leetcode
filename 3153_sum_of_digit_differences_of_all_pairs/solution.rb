# LeetCode 3153 - Sum of Digit Differences of All Pairs
# https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

# @param {Integer[]} nums
# @return {Integer}
def sum_digit_differences(nums)
  n = nums.length
  m = 0
  x = nums[0]
  while x > 0
    m += 1
    x /= 10
  end
  m = 1 if m == 0
  ans = 0
  vals = nums.dup
  m.times do
    cnt = Array.new(10, 0)
    n.times do |i|
      cnt[vals[i] % 10] += 1
      vals[i] /= 10
    end
    cnt.each { |v| ans += v * (n - v) }
  end
  ans / 2
end
