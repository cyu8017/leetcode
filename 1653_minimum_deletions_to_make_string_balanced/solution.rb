# LeetCode 1653 - Minimum Deletions to Make String Balanced
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

# @param {String} s
# @return {Integer}
def minimum_deletions(s)
  b = 0
  ans = 0
  s.each_char do |c|
    if c == "b"
      b += 1
    else
      ans = [ans + 1, b].min
    end
  end
  ans
end
