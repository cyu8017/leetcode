# LeetCode 2031 - Count Subarrays With More Ones Than Zeros
# https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

class Fenwick
  def initialize(n)
    @bit = Array.new(n + 2, 0)
  end

  def add(i, v)
    while i < @bit.length
      @bit[i] += v
      i += i & -i
    end
  end

  def sum(i)
    s = 0
    while i > 0
      s += @bit[i]
      i -= i & -i
    end
    s
  end
end

# @param {Integer[]} nums
# @return {Integer}
def subarrays_with_more_zeros_than_ones(nums)
  mod = 10**9 + 7
  n = nums.length
  offset = n + 1
  fw = Fenwick.new(2 * n + 5)
  pref = 0
  ans = 0
  fw.add(offset, 1)
  nums.each do |x|
    pref += x == 1 ? 1 : -1
    idx = pref + offset
    ans = (ans + fw.sum(idx - 1)) % mod
    fw.add(idx, 1)
  end
  ans
end

alias solve subarrays_with_more_zeros_than_ones
