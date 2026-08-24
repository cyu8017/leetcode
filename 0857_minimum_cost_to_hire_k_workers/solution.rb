# LeetCode 0857 - Minimum Cost to Hire K Workers
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

class MaxHeap
  def initialize
    @a = []
  end

  def size
    @a.size
  end

  def push(item)
    @a << item
    i = @a.size - 1
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
      l = i * 2 + 1
      r = l + 1
      break if l >= @a.size

      largest = r < @a.size && @a[r] > @a[l] ? r : l
      break if @a[i] >= @a[largest]

      @a[i], @a[largest] = @a[largest], @a[i]
      i = largest
    end
    top
  end
end

# @param {Integer[]} quality
# @param {Integer[]} wage
# @param {Integer} k
# @return {Float}
def mincost_to_hire_workers(quality, wage, k)
  workers = quality.zip(wage).map { |q, w| [w.to_f / q, q] }.sort
  heap = MaxHeap.new
  total_q = 0
  ans = Float::INFINITY
  workers.each do |ratio, q|
    heap.push(q)
    total_q += q
    total_q -= heap.pop if heap.size > k
    ans = [ans, total_q * ratio].min if heap.size == k
  end
  ans
end
