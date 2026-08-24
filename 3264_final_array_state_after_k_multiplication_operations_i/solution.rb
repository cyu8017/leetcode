# LeetCode 3264 - Final Array State After K Multiplication Operations I
# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

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
  h = MinHeap.new
  nums.each_with_index { |v, i| h.push([v, i]) }
  k.times do
    cur = h.pop
    v = cur[0] * multiplier
    i = cur[1]
    nums[i] = v
    h.push([v, i])
  end
  nums
end
