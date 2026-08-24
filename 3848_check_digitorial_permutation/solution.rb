# LeetCode 3848 - Check Digitorial Permutation
# https://leetcode.com/problems/check-digitorial-permutation/

# @param {Integer} n
# @return {Boolean}
def is_digitorial_permutation(n)
  f = Array.new(10, 0)
  f[0] = 1
  (1...10).each { |i| f[i] = f[i - 1] * i }
  x = 0
  y = n
  while y > 0
    x += f[y % 10]
    y /= 10
  end
  a = x.to_s.chars.sort.join
  b = n.to_s.chars.sort.join
  a == b
end
