# LeetCode 0792 - Number of Matching Subsequences
# https://leetcode.com/problems/number-of-matching-subsequences/

# @param {String} s
# @param {String[]} words
# @return {Integer}
def num_matching_subseq(s, words)
  waiting = Hash.new { |h, k| h[k] = [] }
  words.each { |word| waiting[word[0]] << [word, 1] }

  count = 0
  s.each_char do |ch|
    advance = waiting[ch]
    waiting[ch] = []
    advance.each do |word, idx|
      if idx == word.length
        count += 1
      else
        waiting[word[idx]] << [word, idx + 1]
      end
    end
  end
  count
end
