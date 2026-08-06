# LeetCode 1513 - Number of Substrings With Only 1s
# https://leetcode.com/problems/number-of-substrings-with-only-1s/

# @param {String} s
# @return {Integer}
def num_sub(s)
  ans = run = 0
  s.each_char do |ch|
    run = ch == '1' ? run + 1 : 0
    ans += run
  end
  ans % 1_000_000_007
end
