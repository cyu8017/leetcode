# LeetCode 3039 - Apply Operations to Make String Empty
# https://leetcode.com/problems/apply-operations-to-make-string-empty/

# @param {String} s
# @return {String}
def last_non_empty_string(s)
  cnt = Array.new(26, 0)
  last = Array.new(26, 0)
  mx = 0
  s.length.times do |i|
    c = s[i].ord - 97
    cnt[c] += 1
    last[c] = i
    mx = cnt[c] if cnt[c] > mx
  end
  ans = ""
  s.length.times do |i|
    c = s[i].ord - 97
    ans += s[i] if cnt[c] == mx && last[c] == i
  end
  ans
end
