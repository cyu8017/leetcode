# LeetCode 3163 - String Compression III
# https://leetcode.com/problems/string-compression-iii/

# @param {String} word
# @return {String}
def compressed_string(word)
  ans = []
  n = word.length
  i = 0
  while i < n
    j = i + 1
    j += 1 while j < n && word[j] == word[i]
    k = j - i
    while k > 0
      x = [9, k].min
      ans << x.to_s
      ans << word[i]
      k -= x
    end
    i = j
  end
  ans.join
end
