# LeetCode 1062 - Longest Repeating Substring
# https://leetcode.com/problems/longest-repeating-substring/

# @param {String} s
# @return {Integer}
def longest_repeating_substring(s)
  n = s.length

  has_dup = lambda do |length|
    seen = {}
    (0..(n - length)).each do |i|
      sub = s[i, length]
      return true if seen[sub]

      seen[sub] = true
    end
    false
  end

  lo = 1
  hi = n - 1
  ans = 0
  while lo <= hi
    mid = (lo + hi) / 2
    if has_dup.call(mid)
      ans = mid
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  ans
end
