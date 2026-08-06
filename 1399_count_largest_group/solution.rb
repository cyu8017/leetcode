# LeetCode 1399 - Count Largest Group
# https://leetcode.com/problems/count-largest-group/

def count_largest_group(n)
  c = Hash.new(0)
  (1..n).each { |x| c[x.digits.sum] += 1 }
  m = c.values.max
  c.values.count { |v| v == m }
end
