# LeetCode 3915 - Maximum Sum of Alternating Subsequence With Distance at Least K
# https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

class Fenwick3915
  def initialize(n)
    @f = Array.new(n, 0)
  end

  def update(i, val)
    while i < @f.length
      @f[i] = [@f[i], val].max
      i += i & -i
    end
  end

  def pre_max(i)
    res = 0
    while i > 0
      res = [res, @f[i]].max
      i &= i - 1
    end
    res
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_alternating_sum(nums, k)
  sorted_nums = nums.sort
  m = 0
  sorted_nums.length.times do |i|
    if i == 0 || sorted_nums[i] != sorted_nums[i - 1]
      sorted_nums[m] = sorted_nums[i]
      m += 1
    end
  end
  sorted_nums = sorted_nums[0, m]
  n = nums.length
  f_inc = Array.new(n, 0)
  f_dec = Array.new(n, 0)
  inc = Fenwick3915.new(m + 1)
  dec = Fenwick3915.new(m + 1)
  ans = 0
  ranks = Array.new(n, 0)
  n.times do |i|
    x = nums[i]
    if i >= k
      j = ranks[i - k]
      inc.update(m - j, f_inc[i - k])
      dec.update(j + 1, f_dec[i - k])
    end
    lo = 0
    hi = sorted_nums.length
    while lo < hi
      mid = (lo + hi) >> 1
      if sorted_nums[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    ranks[i] = lo
    f_inc[i] = dec.pre_max(lo) + x
    f_dec[i] = inc.pre_max(m - 1 - lo) + x
    ans = [ans, [f_inc[i], f_dec[i]].max].max
  end
  ans
end
