# LeetCode 2938 - Separate Black and White Balls
# https://leetcode.com/problems/separate-black-and-white-balls/

# @param {String} s
# @return {Integer}
def minimum_steps(s)
  ans = 0
  zeros = 0
  (s.length - 1).downto(0) do |i|
    if s[i] == "0"
      zeros += 1
    else
      ans += zeros
    end
  end
  ans
end
