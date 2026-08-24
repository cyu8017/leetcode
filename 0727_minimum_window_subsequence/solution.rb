# LeetCode 0727 - Minimum Window Subsequence
# https://leetcode.com/problems/minimum-window-subsequence/

# @param {String} s1
# @param {String} s2
# @return {String}
def min_window(s1, s2)
  m = s1.length
  n = s2.length
  best = ""
  i = 0
  while i < m
    j = 0
    k = i
    while k < m && j < n
      j += 1 if s1[k] == s2[j]
      k += 1
    end
    break if j < n

    last = k - 1
    j = n - 1
    k = last
    while j >= 0
      j -= 1 if s1[k] == s2[j]
      k -= 1
    end
    start = k + 1
    best = s1[start..last] if best.empty? || last - start + 1 < best.length
    i = start + 1
  end
  best
end
