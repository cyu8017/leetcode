# LeetCode 2957 - Remove Adjacent Almost-Equal Characters
# https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

# @param {String} word
# @return {Integer}
def remove_almost_equal_characters(word)
  ans = 0
  i = 1
  n = word.length
  while i < n
    if (word[i].ord - word[i - 1].ord).abs <= 1
      ans += 1
      i += 2
    else
      i += 1
    end
  end
  ans
end
