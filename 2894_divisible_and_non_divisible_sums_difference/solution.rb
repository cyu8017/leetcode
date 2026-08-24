# LeetCode 2894 - Divisible and Non-divisible Sums Difference
# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def difference_of_sums(n, m)
  num1 = num2 = 0
  (1..n).each do |i|
    if i % m == 0
      num2 += i
    else
      num1 += i
    end
  end
  num1 - num2
end
