# LeetCode 1876 - Substrings of Size Three with Distinct Characters
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

# @param {String} s
# @return {Integer}
def count_good_substrings(s)
  return 0 if s.length < 3

  count = 0
  (0..s.length - 3).each do |i|
    window = s[i, 3]
    count += 1 if window.chars.uniq.length == 3
  end
  count
end
