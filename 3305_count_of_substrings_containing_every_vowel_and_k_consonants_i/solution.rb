# LeetCode 3305 - Count of Substrings Containing Every Vowel and K Consonants I
# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/

# @param {String} c
# @return {Boolean}
def vowel_char?(c)
  c == "a" || c == "e" || c == "i" || c == "o" || c == "u"
end

# @param {String} word
# @param {Integer} k
# @return {Integer}
def at_least_vowel_consonant(word, k)
  cnt = {}
  cons = 0
  l = 0
  ans = 0
  word.length.times do |r|
    c = word[r]
    if vowel_char?(c)
      cnt[c] = (cnt[c] || 0) + 1
    else
      cons += 1
    end
    while cnt.length == 5 && cons >= k
      ans += word.length - r
      c2 = word[l]
      if vowel_char?(c2)
        nv = cnt[c2] - 1
        if nv == 0
          cnt.delete(c2)
        else
          cnt[c2] = nv
        end
      else
        cons -= 1
      end
      l += 1
    end
  end
  ans
end

# @param {String} word
# @param {Integer} k
# @return {Integer}
def count_of_substrings(word, k)
  at_least_vowel_consonant(word, k) - at_least_vowel_consonant(word, k + 1)
end
