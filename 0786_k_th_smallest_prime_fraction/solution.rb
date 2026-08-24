# LeetCode 0786 - K-th Smallest Prime Fraction
# https://leetcode.com/problems/k-th-smallest-prime-fraction/

class MinHeap
  def initialize
    @a = []
  end

  def push(item)
    @a << item
    i = @a.size - 1
    while i.positive?
      p = (i - 1) / 2
      break if (@a[p] <=> @a[i]) <= 0

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

      smallest = r < @a.size && (@a[r] <=> @a[l]) < 0 ? r : l
      break if (@a[i] <=> @a[smallest]) <= 0

      @a[i], @a[smallest] = @a[smallest], @a[i]
      i = smallest
    end
    top
  end
end

# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer[]}
def kth_smallest_prime_fraction(arr, k)
  n = arr.length
  heap = MinHeap.new
  (0...n - 1).each { |i| heap.push([arr[i].to_f / arr[-1], i, n - 1]) }
  (k - 1).times do
    _, i, j = heap.pop
    heap.push([arr[i].to_f / arr[j - 1], i, j - 1]) if j - 1 > i
  end
  _, i, j = heap.pop
  [arr[i], arr[j]]
end
