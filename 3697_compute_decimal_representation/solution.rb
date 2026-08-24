# LeetCode 3697 - Compute Decimal Representation
# https://leetcode.com/problems/compute-decimal-representation/

# @param {Integer} n
# @return {Integer[]}
def decimal_representation(n)
  ans = []
  p = 1
  while n > 0
    v = n % 10
    n /= 10
    ans << p * v if v != 0
    p *= 10
  end
  ans.reverse
end
