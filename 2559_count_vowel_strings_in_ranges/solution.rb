# LeetCode 2559 - Count Vowel Strings in Ranges
# https://leetcode.com/problems/count-vowel-strings-in-ranges/

# @param {String[]} words
# @param {Integer[][]} queries
# @return {Integer[]}
def vowel_strings(words, queries)
  is_v = lambda { |c| c == "a" || c == "e" || c == "i" || c == "o" || c == "u" }
  n = words.length
  pref = Array.new(n + 1, 0)
  n.times do |i|
    pref[i + 1] = pref[i]
    w = words[i]
    pref[i + 1] += 1 if !w.empty? && is_v.call(w[0]) && is_v.call(w[-1])
  end
  queries.map { |l, r| pref[r + 1] - pref[l] }
end
