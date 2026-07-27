# LeetCode 1675 - Minimize Deviation in Array
# https://leetcode.com/problems/minimize-deviation-in-array/

class MaxHeap1675
  def initialize
    @a = []
  end

  def push(x)
    @a << x
    i = @a.length - 1
    while i.positive?
      p = (i - 1) / 2
      break if @a[p] >= @a[i]

      @a[p], @a[i] = @a[i], @a[p]
      i = p
    end
  end

  def pop
    top = @a[0]
    last = @a.pop
    return top if @a.empty?

    @a[0] = last
    i = 0
    loop do
      l = 2 * i + 1
      r = 2 * i + 2
      largest = i
      largest = l if l < @a.length && @a[l] > @a[largest]
      largest = r if r < @a.length && @a[r] > @a[largest]
      break if largest == i

      @a[i], @a[largest] = @a[largest], @a[i]
      i = largest
    end
    top
  end
end

# @param {Integer[]} nums
# @return {Integer}
def minimum_deviation(nums)
  h = MaxHeap1675.new
  mn = 10**20
  nums.each do |x|
    x *= 2 if x.odd?
    mn = [mn, x].min
    h.push(x)
  end
  ans = 10**20
  loop do
    x = h.pop
    ans = [ans, x - mn].min
    return ans if x.odd?

    x /= 2
    mn = [mn, x].min
    h.push(x)
  end
end
