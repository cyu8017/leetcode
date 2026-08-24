# LeetCode 0884 - Uncommon Words from Two Sentences
# https://leetcode.com/problems/uncommon-words-from-two-sentences/

# @param {String} s1
# @param {String} s2
# @return {String[]}
def uncommon_from_sentences(s1, s2)
  count = Hash.new(0)
  (s1 + " " + s2).split.each { |w| count[w] += 1 }
  count.select { |_, c| c == 1 }.keys
end
