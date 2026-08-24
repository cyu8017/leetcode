# LeetCode 2233 - Maximum Product After K Increments
# https://leetcode.com/problems/maximum-product-after-k-increments/

class MinHeap
  def initialize(arr)
    @a = arr.dup
    ((@a.length / 2) - 1).downto(0) { |i| down(i) }
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    top = @a[0]
    last = @a.pop
    unless @a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  def each(&block)
    @a.each(&block)
  end

  private

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if @a[i] >= @a[p]

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
      s = l if l < n && @a[l] < @a[s]
      s = r if r < n && @a[r] < @a[s]
      break if s == i

      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_product(nums, k)
  mod = 1_000_000_007
  h = MinHeap.new(nums)
  k.times { h.push(h.pop + 1) }
  ans = 1
  h.each { |x| ans = ans * x % mod }
  ans
end
