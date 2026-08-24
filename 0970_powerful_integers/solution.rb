# LeetCode 0970 - Powerful Integers
# https://leetcode.com/problems/powerful-integers/

# @param {Integer} x
# @param {Integer} y
# @param {Integer} bound
# @return {Integer[]}
def powerful_integers(x, y, bound)
  ans = {}
  a = 1
  while a < bound
    b = 1
    while a + b <= bound
      ans[a + b] = true
      break if y == 1

      b *= y
    end
    break if x == 1

    a *= x
  end
  ans.keys.sort
end
