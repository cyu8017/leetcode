# LeetCode 1417 - Reformat The String
# https://leetcode.com/problems/reformat-the-string/

def reformat(s)
  letters = s.chars.select { |c| c =~ /[a-zA-Z]/ }
  digits = s.chars.select { |c| c =~ /\d/ }
  return '' if (letters.length - digits.length).abs > 1
  letters, digits = digits, letters if digits.length >= letters.length
  answer = []
  letters.each_with_index do |char, i|
    answer << char
    answer << digits[i] if i < digits.length
  end
  answer.join
end
