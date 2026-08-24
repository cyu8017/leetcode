# LeetCode 2375 - Construct Smallest Number From DI String
# https://leetcode.com/problems/construct-smallest-number-from-di-string/

# @param {String} pattern
# @return {String}
def smallest_number(pattern)
  n = pattern.length
  ans = (0..n).map { |i| (49 + i).chr }
  i = 0
  while i < n
    if pattern[i] == "I"
      i += 1
      next
    end
    j = i
    j += 1 while j < n && pattern[j] == "D"
    l = i
    r = j
    while l < r
      ans[l], ans[r] = ans[r], ans[l]
      l += 1
      r -= 1
    end
    i = j
  end
  ans.join
end
