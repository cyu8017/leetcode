# LeetCode 1952 - Three Divisors
# https://leetcode.com/problems/three-divisors/

# @param {Integer} n
# @return {Boolean}
def is_three(n)
  root = (n**0.5).to_i
  return false if root * root != n || root < 2
  i = 2
  while i * i <= root
    return false if (root % i).zero?
    i += 1
  end
  true
end
