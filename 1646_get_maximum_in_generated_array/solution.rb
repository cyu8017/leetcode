# LeetCode 1646 - Get Maximum in Generated Array
# https://leetcode.com/problems/get-maximum-in-generated-array/

# @param {Integer} n
# @return {Integer}
def get_maximum_generated(n)
  return n if n < 2

  a = Array.new(n + 1, 0)
  a[1] = 1
  (2..n).each do |i|
    a[i] = i.even? ? a[i / 2] : a[i / 2] + a[i / 2 + 1]
  end
  a.max
end
