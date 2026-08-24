# LeetCode 2744 - Find Maximum Number of String Pairs
# https://leetcode.com/problems/find-maximum-number-of-string-pairs/

# @param {String[]} words
# @return {Integer}
def maximum_number_of_string_pairs(words)
  freq = Hash.new(0)
  ans = 0
  words.each do |w|
    rev = w.reverse
    c = freq[rev]
    if c > 0
      ans += 1
      freq[rev] = c - 1
    else
      freq[w] += 1
    end
  end
  ans
end
