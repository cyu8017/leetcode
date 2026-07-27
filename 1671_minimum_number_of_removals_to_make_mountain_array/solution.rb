# LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

def _lis_lengths(a)
  d = []
  out = []
  a.each do |x|
    i = d.bsearch_index { |y| y >= x } || d.length
    if i == d.length
      d << x
    else
      d[i] = x
    end
    out << i + 1
  end
  out
end

# @param {Integer[]} nums
# @return {Integer}
def minimum_mountain_removals(nums)
  l = _lis_lengths(nums)
  r = _lis_lengths(nums.reverse).reverse
  n = nums.length
  best = 0
  n.times do |i|
    next unless l[i] > 1 && r[i] > 1

    best = [best, l[i] + r[i] - 1].max
  end
  n - best
end
