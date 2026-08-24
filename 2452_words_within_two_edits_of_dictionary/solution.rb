# LeetCode 2452 - Words Within Two Edits of Dictionary
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

# @param {String[]} queries
# @param {String[]} dictionary
# @return {String[]}
def two_edit_words(queries, dictionary)
  ans = []
  queries.each do |q|
    ok = false
    dictionary.each do |d|
      df = 0
      (0...q.length).each do |i|
        if q[i] != d[i]
          df += 1
          break if df > 2
        end
      end
      if df <= 2
        ok = true
        break
      end
    end
    ans << q if ok
  end
  ans
end
