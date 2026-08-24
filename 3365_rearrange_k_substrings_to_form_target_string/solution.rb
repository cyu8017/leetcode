# LeetCode 3365 - Rearrange K Substrings to Form Target String
# https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

# @param {String} s
# @param {String} t
# @param {Integer} k
# @return {Boolean}
def is_possible_to_rearrange(s, t, k)
  n = s.length
  sz = n / k
  cnt = {}
  (0...n).step(sz) do |i|
    a = s[i, sz]
    b = t[i, sz]
    cnt[a] = (cnt[a] || 0) + 1
    cnt[b] = (cnt[b] || 0) - 1
  end
  cnt.values.all?(&:zero?)
end
