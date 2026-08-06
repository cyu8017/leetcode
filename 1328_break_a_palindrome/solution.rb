# LeetCode 1328 - Break A Palindrome
# https://leetcode.com/problems/break-a-palindrome/

def break_palindrome(palindrome)
  return '' if palindrome.length == 1
  chars = palindrome.chars
  (chars.length / 2).times do |i|
    if chars[i] != 'a'
      chars[i] = 'a'
      return chars.join
    end
  end
  chars[-1] = 'b'
  chars.join
end
