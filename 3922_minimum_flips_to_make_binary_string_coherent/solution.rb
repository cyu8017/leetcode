# LeetCode 3922 - Minimum Flips to Make Binary String Coherent
# https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

# @param {String} s
# @return {Integer}
def min_flips(s)
  ones = s.count("1")
  answer = ones
  answer = ones - 1 if ones > 0
  zeros = s.length - ones
  answer = [answer, zeros].min
  if s.length >= 2
    cost = 0
    s.length.times do |i|
      want = (i == 0 || i == s.length - 1) ? "1" : "0"
      cost += 1 if s[i] != want
    end
    answer = [answer, cost].min
  end
  answer
end
