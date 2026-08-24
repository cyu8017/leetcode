# LeetCode 2178 - Maximum Split of Positive Even Integers
# https://leetcode.com/problems/maximum-split-of-positive-even-integers/

# @param {Integer} final_sum
# @return {Integer[]}
def maximum_even_split(final_sum)
  return [] if final_sum.odd?

  ans = []
  x = 2
  while x <= final_sum
    ans << x
    final_sum -= x
    x += 2
  end
  ans[-1] += final_sum
  ans
end
