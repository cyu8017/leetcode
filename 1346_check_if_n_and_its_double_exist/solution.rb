# LeetCode 1346 - Check If N And Its Double Exist
# https://leetcode.com/problems/check-if-n-and-its-double-exist/

def check_if_exist(arr)
  seen = {}
  arr.each do |value|
    return true if seen[2 * value] || (value.even? && seen[value / 2])
    seen[value] = true
  end
  false
end
