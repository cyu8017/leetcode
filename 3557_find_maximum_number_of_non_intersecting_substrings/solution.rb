# LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
# https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

# @param {String} word
# @return {Integer}
def max_substrings(word)
  ans = 0
  first = {}
  word.each_char.with_index do |c, i|
    if !first.key?(c)
      first[c] = i
    elsif i - first[c] + 1 >= 4
      ans += 1
      first.clear
    end
  end
  ans
end
