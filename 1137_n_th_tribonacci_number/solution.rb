# LeetCode 1137 - N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/

# @param {Integer} n
# @return {Integer}
def tribonacci(n)
  return 0 if n == 0
  return 1 if n <= 2
  a = 0
  b = 1
  c = 1
  (3..n).each do
    a, b, c = b, c, a + b + c
  end
  c
end
