# LeetCode 2193 - Minimum Number of Moves to Make Palindrome
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

# @param {String} s
# @return {Integer}
def min_moves_to_make_palindrome(s)
  b = s.chars
  ans = 0
  while b.length > 1
    j = b.length - 1
    j -= 1 while j > 0 && b[j] != b[0]
    if j == 0
      ans += b.length / 2
      b.shift
      next
    end
    ans += b.length - 1 - j
    b.delete_at(j)
    b.shift
  end
  ans
end
