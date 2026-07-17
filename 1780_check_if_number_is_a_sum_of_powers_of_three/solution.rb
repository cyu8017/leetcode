# LeetCode 1780 - Check if Number is a Sum of Powers of Three
# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

# @param {Integer} n
# @return {Boolean}
def check_powers_of_three(n)
  while n > 0
    return false if n % 3 == 2
    n /= 3
  end
  true
end
