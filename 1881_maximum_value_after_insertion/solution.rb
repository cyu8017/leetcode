# LeetCode 1881 - Maximum Value after Insertion
# https://leetcode.com/problems/maximum-value-after-insertion/

# @param {String} n
# @param {Integer} x
# @return {String}
def max_value(n, x)
  neg = n[0] == "-"
  start = neg ? 1 : 0
  (start...n.length).each do |i|
    d = n[i].to_i
    if neg
      return n[0...i] + x.to_s + n[i..] if d > x
    else
      return n[0...i] + x.to_s + n[i..] if d < x
    end
  end
  n + x.to_s
end
