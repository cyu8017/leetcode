# LeetCode 3760 - Maximum Substrings with Distinct Start
# https://leetcode.com/problems/maximum-substrings-with-distinct-start/

# @param {String} s
# @return {Integer}
def max_distinct(s)
  cnt = Array.new(26, 0)
  ans = 0
  s.each_char do |c|
    i = c.ord - 97
    cnt[i] += 1
    ans += 1 if cnt[i] == 1
  end
  ans
end
