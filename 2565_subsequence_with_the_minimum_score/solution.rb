# LeetCode 2565 - Subsequence With the Minimum Score
# https://leetcode.com/problems/subsequence-with-the-minimum-score/

# @param {String} s
# @param {String} t
# @return {Integer}
def minimum_score(s, t)
  n = s.length
  m = t.length
  left = Array.new(m, -1)
  right = Array.new(m, -1)
  j = 0
  i = 0
  while i < n && j < m
    if s[i] == t[j]
      left[j] = i
      j += 1
    end
    i += 1
  end
  j = m - 1
  i = n - 1
  while i >= 0 && j >= 0
    if s[i] == t[j]
      right[j] = i
      j -= 1
    end
    i -= 1
  end
  return 0 if m > 0 && left[m - 1] != -1

  ans = m
  m.times do |i|
    next unless right[i] != -1

    ans = i if i < ans
    break
  end
  (m - 1).downto(0) do |i|
    next unless left[i] != -1

    rem = m - 1 - i
    ans = rem if rem < ans
    break
  end
  j = 0
  m.times do |i|
    break if left[i] == -1

    j += 1 while j < m && (right[j] == -1 || right[j] <= left[i])
    if j < m
      rem = j - i - 1
      ans = rem if rem < ans
    end
  end
  ans
end
