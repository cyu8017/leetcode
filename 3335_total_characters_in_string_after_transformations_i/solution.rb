# LeetCode 3335 - Total Characters in String After Transformations I
# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

# @param {String} s
# @param {Integer} t
# @return {Integer}
def length_after_transformations(s, t)
  mod = 1_000_000_007
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  t.times do
    ncnt = Array.new(26, 0)
    25.times { |i| ncnt[i + 1] = (ncnt[i + 1] + cnt[i]) % mod }
    ncnt[0] = (ncnt[0] + cnt[25]) % mod
    ncnt[1] = (ncnt[1] + cnt[25]) % mod
    cnt = ncnt
  end
  ans = 0
  cnt.each { |v| ans = (ans + v) % mod }
  ans
end
