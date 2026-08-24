# LeetCode 2208 - Minimum Operations to Halve Array Sum
# https://leetcode.com/problems/minimum-operations-to-halve-array-sum/

class MinHeap
  def initialize
    @a = []
  end

  def push(x)
    @a << x
    up(@a.length - 1)
  end

  def pop
    return nil if @a.empty?

    top = @a[0]
    last = @a.pop
    unless @a.empty?
      @a[0] = last
      down(0)
    end
    top
  end

  private

  def up(i)
    while i > 0
      p = (i - 1) >> 1
      break if @a[i] <= @a[p]

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
      s = l if l < n && @a[l] > @a[s]
      s = r if r < n && @a[r] > @a[s]
      break if s == i

      @a[i], @a[s] = @a[s], @a[i]
      i = s
    end
  end
end

# @param {Integer[]} nums
# @return {Integer}
def halve_array(nums)
  h = MinHeap.new
  sum = 0.0
  nums.each do |x|
    h.push(x.to_f)
    sum += x
  end
  target = sum / 2.0
  ans = 0
  while sum > target
    top = h.pop
    x = top / 2.0
    sum -= x
    h.push(x)
    ans += 1
  end
  ans
end
