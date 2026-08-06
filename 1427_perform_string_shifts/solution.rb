# LeetCode 1427 - Perform String Shifts
# https://leetcode.com/problems/perform-string-shifts/

def string_shift(s, shift)
  offset = 0
  shift.each { |direction, amount| offset += direction == 1 ? amount : -amount }
  offset %= s.length
  offset == 0 ? s : s[-offset..] + s[0...-offset]
end
