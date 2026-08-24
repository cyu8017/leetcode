# LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

# @param {String[]} words
# @return {Integer}
def longest_palindrome(words)
  freq = Hash.new(0)
  words.each { |w| freq[w] += 1 }
  ans = 0
  center = false
  freq.each do |w, c|
    rev = w[1] + w[0]
    if w[0] == w[1]
      ans += (c / 2) * 4
      center = true if c.odd?
    elsif w < rev
      ans += [c, freq[rev]].min * 4
    end
  end
  ans += 2 if center
  ans
end
