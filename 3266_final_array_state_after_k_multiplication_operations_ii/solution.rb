# LeetCode 3266 - Final Array State After K Multiplication Operations II
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/

class MinHeap
  def initialize
    @a = []
  end

  def cmp(x, y)
    x[0] != y[0] ? x[0] <=> y[0] : x[1] <=> y[1]
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    return nil if @a.empty?
    top = @a[0]
    last = @a.pop
    if !@a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def size
    @a.length
  end

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if cmp(@a[i], @a[p]) >= 0
      @a[i], @a[p] = @a[p], @a[i]
      i = p
    end
  end

  def down(i)
    n = @a.length
    loop do
      s = i
      l = i * 2 + 1
      r = l + 1
      s = l if l < n && cmp(@a[l], @a[s]) < 0
      s = r if r < n && cmp(@a[r], @a[s]) < 0
      break if s == i
      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} multiplier
# @return {Integer[]}
def get_final_state(nums, k, multiplier)
  mod = 1_000_000_007
  mod_pow = lambda do |a, e, md|
    r = 1
    a %= md
    while e > 0
      r = (r * a) % md if (e & 1) != 0
      a = (a * a) % md
      e >>= 1
    end
    r
  end
  return nums if multiplier == 1
  h = MinHeap.new
  max_v = 0
  nums.each_with_index do |v, i|
    h.push([v, i])
    max_v = v if v > max_v
  end
  while k > 0 && h.size > 0
    cur = h.pop
    v = cur[0]
    i = cur[1]
    if v * multiplier > max_v && k >= nums.length
      h.push([v, i])
      break
    end
    nv = v * multiplier
    nums[i] = nv
    max_v = nv if nv > max_v
    h.push([nv, i])
    k -= 1
  end
  if k > 0
    nn = nums.length
    full = k / nn
    rem = k % nn
    pow_full = mod_pow.call(multiplier, full, mod)
    (0...nn).each { |i| nums[i] = (nums[i] * pow_full) % mod }
    hh = MinHeap.new
    nums.each_with_index { |v, i| hh.push([v, i]) }
    rem.times do
      cur = hh.pop
      v = (cur[0] * multiplier) % mod
      i = cur[1]
      nums[i] = v
      hh.push([v, i])
    end
    (0...nn).each { |i| nums[i] %= mod }
  else
    nums.each_index { |i| nums[i] %= mod }
  end
  nums
end
