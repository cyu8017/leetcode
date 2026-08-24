# LeetCode 2506 - Count Pairs Of Similar Strings
# https://leetcode.com/problems/count-pairs-of-similar-strings/

# @param {String[]} words
# @return {Integer}
def similar_pairs(words)
  freq = Hash.new(0)
  ans = 0
  words.each do |w|
    mask = 0
    w.each_byte { |b| mask |= 1 << (b - 97) }
    ans += freq[mask]
    freq[mask] += 1
  end
  ans
end
