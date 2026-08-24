# LeetCode 2310 - Sum of Numbers With Units Digit K
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

# @param {Integer} num
# @param {Integer} k
# @return {Integer}
def minimum_numbers(num, k)
  return 0 if num == 0
  (1..10).each do |count|
    return count if count * k % 10 == num % 10 && count * k <= num
  end
  -1
end
