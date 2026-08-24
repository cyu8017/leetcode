# LeetCode 0916 - Word Subsets
# https://leetcode.com/problems/word-subsets/

# @param {String[]} words1
# @param {String[]} words2
# @return {String[]}
def word_subsets(words1, words2)
  need = Hash.new(0)
  words2.each do |w|
    cnt = Hash.new(0)
    w.each_char { |ch| cnt[ch] += 1 }
    cnt.each { |ch, c| need[ch] = c if c > need[ch] }
  end
  words1.select do |w|
    cnt = Hash.new(0)
    w.each_char { |ch| cnt[ch] += 1 }
    need.all? { |ch, c| cnt[ch] >= c }
  end
end
