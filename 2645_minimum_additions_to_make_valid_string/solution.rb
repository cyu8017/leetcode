# LeetCode 2645 - Minimum Additions to Make Valid String
# https://leetcode.com/problems/minimum-additions-to-make-valid-string/

# @param {String} word
# @return {Integer}
def add_minimum(word)
  ans = 0
  expect = 0
  i = 0
  n = word.length
  while i < n
    need = (97 + expect).chr
    if word[i] == need
      i += 1
    else
      ans += 1
    end
    expect = (expect + 1) % 3
  end
  ans += (3 - expect) % 3
  ans
end
