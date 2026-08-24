# LeetCode 3448 - Count Substrings Divisible By Last Digit
# https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

# @param {String} s
# @return {Integer}
def count_substrings(s)
  ans = 0
  n = s.length
  (0...n).each do |r|
    last = s[r].ord - 48
    next if last == 0

    mod = 0
    p = 1 % last
    r.downto(0) do |l|
      mod = (mod + (s[l].ord - 48) * p) % last
      p = (p * 10) % last
      ans += 1 if mod == 0
    end
  end
  ans
end
