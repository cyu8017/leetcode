# LeetCode 3013 - Divide an Array Into Subarrays With Minimum Cost II
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/

class BITI
  attr_reader :c, :n

  def initialize(n_)
    @n = n_
    @c = Array.new(n_ + 1, 0)
  end

  def upd(x, d)
    while x <= @n
      @c[x] += d
      x += x & -x
    end
  end

  def qry(x)
    s = 0
    while x > 0
      s += @c[x]
      x -= x & -x
    end
    s
  end
end

class BITL
  attr_reader :c, :n

  def initialize(n_)
    @n = n_
    @c = Array.new(n_ + 1, 0)
  end

  def upd(x, d)
    while x <= @n
      @c[x] += d
      x += x & -x
    end
  end

  def qry(x)
    s = 0
    while x > 0
      s += @c[x]
      x -= x & -x
    end
    s
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} dist
# @return {Integer}
def minimum_cost(nums, k, dist)
  k -= 1
  n = nums.length
  uniq = nums.sort
  write = 0
  uniq.each do |v|
    if write == 0 || v != uniq[write - 1]
      uniq[write] = v
      write += 1
    end
  end
  uniq = uniq[0...write]
  m = uniq.length
  cnt = BITI.new(m + 2)
  sbit = BITL.new(m + 2)
  (1..[dist + 1, n - 1].min).each do |i|
    r = lower_bound(uniq, nums[i]) + 1
    cnt.upd(r, 1)
    sbit.upd(r, nums[i])
  end
  finish = [dist + 1, n - 1].min
  kk = [k, finish].min
  ans = nums[0] + sum_smallest(cnt, sbit, uniq, m, kk)
  (dist + 2...n).each do |i|
    rem = nums[i - dist - 1]
    r1 = lower_bound(uniq, rem) + 1
    cnt.upd(r1, -1)
    sbit.upd(r1, -rem)
    add = nums[i]
    r2 = lower_bound(uniq, add) + 1
    cnt.upd(r2, 1)
    sbit.upd(r2, add)
    kk = [k, dist + 1].min
    cand = nums[0] + sum_smallest(cnt, sbit, uniq, m, kk)
    ans = cand if cand < ans
  end
  ans
end

def bit_kth(cnt, m, k)
  idx = 0
  bit = 1 << 20
  while bit != 0
    nidx = idx + bit
    if nidx <= m && cnt.c[nidx] < k
      k -= cnt.c[nidx]
      idx = nidx
    end
    bit >>= 1
  end
  idx + 1
end

def sum_smallest(cnt, sbit, uniq, m, kk)
  return 0 if kk <= 0

  r = bit_kth(cnt, m, kk)
  before = cnt.qry(r - 1)
  s = sbit.qry(r - 1)
  s += (kk - before) * uniq[r - 1]
  s
end

def lower_bound(arr, x)
  lo = 0
  hi = arr.length
  while lo < hi
    mid = (lo + hi) >> 1
    if arr[mid] < x
      lo = mid + 1
    else
      hi = mid
    end
  end
  lo
end
