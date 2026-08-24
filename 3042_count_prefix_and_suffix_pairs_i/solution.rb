# LeetCode 3042 - Count Prefix and Suffix Pairs I
# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

# @param {String[]} words
# @return {Integer}
def count_prefix_suffix_pairs(words)
  ans = 0
  words.length.times do |i|
    s = words[i]
    (i + 1...words.length).each do |j|
      t = words[j]
      ans += 1 if t.length >= s.length && t.start_with?(s) && t.end_with?(s)
    end
  end
  ans
end
