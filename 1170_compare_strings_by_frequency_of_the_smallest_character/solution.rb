# LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

# @param {String[]} queries
# @param {String[]} words
# @return {Integer[]}
def num_smaller_by_frequency(queries, words)
  f = ->(s) { s.count(s.chars.min) }
  freqs = words.map { |w| f.call(w) }.sort
  queries.map do |q|
    fq = f.call(q)
    idx = freqs.bsearch_index { |x| x > fq } || freqs.length
    freqs.length - idx
  end
end
