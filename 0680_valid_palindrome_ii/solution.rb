# LeetCode 0680 - Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/

# @param {String} s
# @return {Boolean}
def valid_palindrome(s)
  is_palindrome = lambda do |left, right|
    while left < right
      return false if s[left] != s[right]

      left += 1
      right -= 1
    end
    true
  end

  left = 0
  right = s.length - 1
  while left < right
    if s[left] != s[right]
      return is_palindrome.call(left + 1, right) || is_palindrome.call(left, right - 1)
    end

    left += 1
    right -= 1
  end
  true
end
