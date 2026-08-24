# LeetCode 2380 - Time Needed to Rearrange a Binary String
# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

# @param {String} s
# @return {Integer}
def seconds_to_remove_occurrences(s)
  ans = 0
  zeros = 0
  s.each_char do |c|
    if c == "0"
      zeros += 1
    elsif zeros > 0
      ans = [ans + 1, zeros].max
    end
  end
  ans
end
