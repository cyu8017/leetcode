# LeetCode 2414 - Length of the Longest Alphabetical Continuous Substring
# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

# @param {String} s
# @return {Integer}
def longest_continuous_substring(s)
  ans = 1
  cur = 1
  (1...s.length).each do |i|
    if s[i].ord == s[i - 1].ord + 1
      cur += 1
      ans = cur if cur > ans
    else
      cur = 1
    end
  end
  ans
end
