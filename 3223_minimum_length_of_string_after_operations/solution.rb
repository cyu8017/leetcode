# LeetCode 3223 - Minimum Length of String After Operations
# https://leetcode.com/problems/minimum-length-of-string-after-operations/

# @param {String} s
# @return {Integer}
def minimum_length(s)
  cnt = Array.new(26, 0)
  s.each_char { |ch| cnt[ch.ord - 97] += 1 }
  ans = 0
  cnt.each do |x|
    next if x <= 0
    ans += (x & 1) != 0 ? 1 : 2
  end
  ans
end
