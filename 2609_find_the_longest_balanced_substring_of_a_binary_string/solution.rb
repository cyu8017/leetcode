# LeetCode 2609 - Find the Longest Balanced Substring of a Binary String
# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

# @param {String} s
# @return {Integer}
def find_the_longest_balanced_substring(s)
  ans = 0
  zeros = 0
  ones = 0
  s.each_char do |c|
    if c == "0"
      zeros = ones = 0 if ones > 0
      zeros += 1
    else
      ones += 1
      cur = [ones, zeros].min
      ans = 2 * cur if 2 * cur > ans
    end
  end
  ans
end
