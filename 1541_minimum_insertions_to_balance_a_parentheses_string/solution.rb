# LeetCode 1541 - Minimum Insertions to Balance a Parentheses String
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

# @param {String} s
# @return {Integer}
def min_insertions(s)
  insertions = needed = 0
  s.each_char do |ch|
    if ch == '('
      needed += 2
      if needed.odd?
        insertions += 1
        needed -= 1
      end
    else
      needed -= 1
      if needed < 0
        insertions += 1
        needed = 1
      end
    end
  end
  insertions + needed
end
