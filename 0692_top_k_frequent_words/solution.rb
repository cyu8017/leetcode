# LeetCode 0692 - Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/

# @param {String[]} words
# @param {Integer} k
# @return {String[]}
def top_k_frequent(words, k)
  counts = Hash.new(0)
  words.each { |w| counts[w] += 1 }
  ordered = counts.keys.sort_by { |w| [-counts[w], w] }
  ordered[0, k]
end
