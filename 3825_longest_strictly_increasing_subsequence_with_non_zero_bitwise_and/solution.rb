# LeetCode 3825 - Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND
# https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/

# @param {Integer[]} nums
# @return {Integer}
def longest_subsequence(nums)
  ans = 0
  mx = nums.max
  m = bit_len_3825(mx)
  (0...m).each do |i|
    arr = []
    nums.each { |x| arr << x if ((x >> i) & 1) != 0 }
    ans = [ans, lis_3825(arr)].max
  end
  ans
end

def bit_len_3825(x)
  return 0 if x == 0
  n = 0
  while x > 0
    n += 1
    x >>= 1
  end
  n
end

def lis_3825(arr)
  g = []
  arr.each do |x|
    lo = 0
    hi = g.length
    while lo < hi
      mid = (lo + hi) >> 1
      if g[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    if lo == g.length
      g << x
    else
      g[lo] = x
    end
  end
  g.length
end
