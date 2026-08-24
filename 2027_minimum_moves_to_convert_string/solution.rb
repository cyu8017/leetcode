# LeetCode 2027 - Minimum Moves to Convert String
# https://leetcode.com/problems/minimum-moves-to-convert-string/

# @param {String} s
# @return {Integer}
def minimum_moves(s)
  ans = 0
  i = 0
  while i < s.length
    if s[i] == "X"
      ans += 1
      i += 3
    else
      i += 1
    end
  end
  ans
end
