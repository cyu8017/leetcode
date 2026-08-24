# LeetCode 2953 - Count Complete Substrings
# https://leetcode.com/problems/count-complete-substrings/

# @param {String} word
# @param {Integer} k
# @return {Integer}
def count_complete_substrings(word, k)
  n = word.length
  ans = 0
  i = 0
  while i < n
    j = i
    j += 1 while j + 1 < n && (word[j + 1].ord - word[j].ord).abs <= 2
    seg = word[i..j]
    m = seg.length
    (1..26).each do |chars|
      length = chars * k
      break if length > m

      freq = Array.new(26, 0)
      unique = 0
      m.times do |r|
        c = seg[r].ord - 97
        freq[c] += 1
        unique += 1 if freq[c] == 1
        if r >= length
          c2 = seg[r - length].ord - 97
          freq[c2] -= 1
          unique -= 1 if freq[c2] == 0
        end
        if r >= length - 1 && unique == chars
          ok = true
          freq.each do |f|
            if f != 0 && f != k
              ok = false
              break
            end
          end
          ans += 1 if ok
        end
      end
    end
    i = j + 1
  end
  ans
end
