# LeetCode 0326 - Power of Three
# https://leetcode.com/problems/power-of-three/

class Solution
  def isPowerOfThree(n)
    return false if n <= 0

    while n % 3 == 0
      n /= 3
    end
    n == 1
  end
end
