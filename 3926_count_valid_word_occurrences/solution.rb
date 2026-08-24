# LeetCode 3926 - Count Valid Word Occurrences
# https://leetcode.com/problems/count-valid-word-occurrences/

# @param {String[]} chunks
# @param {String[]} queries
# @return {Integer[]}
def count_word_occurrences(chunks, queries)
  s = chunks.join
  n = s.length
  cnt = {}
  i = 0
  while i < n
    if s[i] == " " || s[i] == "-"
      i += 1
      next
    end
    j = i
    while j < n && s[j] != " " && (s[j] != "-" || (j + 1 < n && s[j + 1] != " " && s[j + 1] != "-"))
      j += 1
    end
    word = s[i...j]
    cnt[word] = cnt.fetch(word, 0) + 1
    i = j
  end
  queries.map { |q| cnt.fetch(q, 0) }
end
