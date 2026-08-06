# LeetCode 1446 - Consecutive Characters
# https://leetcode.com/problems/consecutive-characters/

def max_power(s)
  answer = run = 1
  (1...s.length).each do |i|
    run = s[i] == s[i - 1] ? run + 1 : 1
    answer = [answer, run].max
  end
  answer
end
