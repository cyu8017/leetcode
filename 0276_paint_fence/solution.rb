# LeetCode 0276 - Paint Fence
# https://leetcode.com/problems/paint-fence/

class Solution
  def numWays(n, k)
    return 0 if n == 0
    return k if n == 1
    return k * k if n == 2

    prev2 = k
    prev1 = k * k
    (3..n).each do
      next_total = (prev1 + prev2) * (k - 1)
      prev2 = prev1
      prev1 = next_total
    end
    prev1
  end
end
