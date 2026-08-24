# LeetCode 3398 - Smallest Substring With Identical Characters I
# https://leetcode.com/problems/smallest-substring-with-identical-characters-i/

# @param {String} s
# @param {Integer} num_ops
# @return {Integer}
def min_length(s, num_ops)
  n = s.length
  ok = lambda do |len|
    return false if len == 0

    ops = 0
    i = 0
    while i < n
      j = i
      j += 1 while j < n && s[j] == s[i]
      ops += (j - i) / (len + 1)
      i = j
    end
    ops <= num_ops
  end
  lo = 1
  hi = n
  while lo < hi
    mid = (lo + hi) / 2
    if ok.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
