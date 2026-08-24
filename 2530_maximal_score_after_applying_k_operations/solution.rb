# LeetCode 2530 - Maximal Score After Applying K Operations
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

class MinHeap
  def initialize(arr = [])
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

  def peek
    @a[0]
  end

  def empty?
    @a.empty?
  end

  def length
    @a.length
  end

  def sum
    @a.sum
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
def max_kelements(nums, k)
  h = MinHeap.new(nums.map { |x| -x })
  ans = 0
  k.times do
    x = -h.pop
    ans += x
    h.push(-((x + 2) / 3))
  end
  ans
end
