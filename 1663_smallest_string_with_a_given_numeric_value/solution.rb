# LeetCode 1663 - Smallest String With A Given Numeric Value
# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

# @param {Integer} n
# @param {Integer} k
# @return {String}
def get_smallest_string(n, k)
  a = Array.new(n, "a")
  k -= n
  (n - 1).downto(0) do |i|
    d = [25, k].min
    a[i] = (97 + d).chr
    k -= d
  end
  a.join
end
