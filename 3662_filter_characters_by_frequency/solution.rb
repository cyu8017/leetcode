# LeetCode 3662 - Filter Characters by Frequency
# https://leetcode.com/problems/filter-characters-by-frequency/

# @param {String} s
# @param {Integer} k
# @return {String}
def filter_characters(s, k)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  s.chars.select { |c| cnt[c.ord - 97] < k }.join
end
