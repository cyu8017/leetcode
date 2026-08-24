# LeetCode 0660 - Remove 9
# https://leetcode.com/problems/remove-9/

# @param {Integer} n
# @return {Integer}
def new_integer(n)
  digits = []
  while n > 0
    digits << (n % 9).to_s
    n /= 9
  end
  digits.empty? ? 0 : digits.reverse.join.to_i
end
