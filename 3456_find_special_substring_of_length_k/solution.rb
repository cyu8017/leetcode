# LeetCode 3456 - Find Special Substring of Length K
# https://leetcode.com/problems/find-special-substring-of-length-k/

# @param {String} s
# @param {Integer} k
# @return {Boolean}
def has_special_substring(s, k)
  n = s.length
  (0..(n - k)).each do |i|
    ok = true
    ((i + 1)...(i + k)).each do |j|
      if s[j] != s[i]
        ok = false
        break
      end
    end
    next unless ok
    next if i > 0 && s[i - 1] == s[i]
    next if i + k < n && s[i + k] == s[i]

    return true
  end
  false
end
