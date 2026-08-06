# LeetCode 1422 - Maximum Score After Splitting A String
# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

def max_score(s)
  ones = s.count('1')
  left_zeros = answer = 0
  s[0...-1].each_char do |char|
    if char == '0'
      left_zeros += 1
    else
      ones -= 1
    end
    answer = [answer, left_zeros + ones].max
  end
  answer
end
