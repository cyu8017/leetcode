# LeetCode 3344 - Maximum Sized Array
# https://leetcode.com/problems/maximum-sized-array/

# @param {Integer} n
# @param {Integer} s
# @return {Boolean}
def sized_array_ok(n, s)
  total = 0
  n.times do |i|
    n.times do |j|
      ij = i | j
      total += ij * (n - 1) * n / 2
      return false if total > s
    end
  end
  total <= s
end

# @param {Integer} s
# @return {Integer}
def max_sized_array(s)
  lo = 1
  hi = 2000
  while lo < hi
    mid = (lo + hi + 1) / 2
    if sized_array_ok(mid, s)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
