# LeetCode 2950 - Number of Divisible Substrings
# https://leetcode.com/problems/number-of-divisible-substrings/

# @param {String} word
# @return {Integer}
def count_divisible_substrings(word)
  vals = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
  ans = 0
  n = word.length
  n.times do |i|
    s = 0
    i.upto(n - 1) do |j|
      s += vals[word[j].ord - 97]
      ans += 1 if s % (j - i + 1) == 0
    end
  end
  ans
end

def solve(*args)
  count_divisible_substrings(*args)
end
