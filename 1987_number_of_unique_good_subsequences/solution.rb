# LeetCode 1987 - Number of Unique Good Subsequences
# https://leetcode.com/problems/number-of-unique-good-subsequences/

# @param {String} binary
# @return {Integer}
def number_of_unique_good_subsequences(binary)
  mod = 10**9 + 7
  ends0 = ends1 = 0
  has0 = false
  binary.each_char do |ch|
    if ch == "0"
      has0 = true
      ends0 = (ends0 + ends1) % mod
    else
      ends1 = (ends0 + ends1 + 1) % mod
    end
  end
  (ends0 + ends1 + (has0 ? 1 : 0)) % mod
end
