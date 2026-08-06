# LeetCode 1309 - Decrypt String From Alphabet To Integer Mapping
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

def freq_alphabets(s)
  answer = []
  i = s.length - 1
  while i >= 0
    if s[i] == '#'
      answer << (96 + s[i - 2, 2].to_i).chr
      i -= 3
    else
      answer << (96 + s[i].to_i).chr
      i -= 1
    end
  end
  answer.reverse.join
end
