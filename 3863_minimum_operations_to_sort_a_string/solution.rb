# LeetCode 3863 - Minimum Operations to Sort a String
# https://leetcode.com/problems/minimum-operations-to-sort-a-string/

# @param {String} s
# @return {Integer}
def min_operations(s)
  n = s.length
  sorted_ok = true
  (1...n).each do |i|
    if s[i] < s[i - 1]
      sorted_ok = false
      break
    end
  end
  return 0 if sorted_ok
  return -1 if n == 2
  mn = s.chars.min
  mx = s.chars.max
  return 1 if s[0] == mn || s[n - 1] == mx
  (1...(n - 1)).each { |i| return 2 if s[i] == mn || s[i] == mx }
  3
end
