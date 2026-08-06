# LeetCode 1297 - Maximum Number of Occurrences of a Substring
# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

# @param {String} s
# @param {Integer} max_letters
# @param {Integer} min_size
# @param {Integer} max_size
# @return {Integer}
def max_freq(s, max_letters, min_size, max_size)
  counts = Hash.new(0)
  (0..(s.length - min_size)).each do |i|
    sub = s[i, min_size]
    counts[sub] += 1 if sub.chars.uniq.length <= max_letters
  end
  counts.empty? ? 0 : counts.values.max
end
