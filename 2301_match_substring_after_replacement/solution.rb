# LeetCode 2301 - Match Substring After Replacement
# https://leetcode.com/problems/match-substring-after-replacement/

# @param {String} s
# @param {String} sub
# @param {String[][]} mappings
# @return {Boolean}
def match_replacement(s, sub, mappings)
  allow = {}
  mappings.each do |a, b|
    allow[(a[0].ord << 8) | b[0].ord] = true
  end
  n = s.length
  mlen = sub.length
  (0..(n - mlen)).each do |i|
    ok = true
    mlen.times do |j|
      a = s[i + j]
      b = sub[j]
      next if a == b || allow.key?((b.ord << 8) | a.ord)

      ok = false
      break
    end
    return true if ok
  end
  false
end
