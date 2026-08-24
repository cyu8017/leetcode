# LeetCode 2542 - Maximum Subsequence Score
# https://leetcode.com/problems/maximum-subsequence-score/

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

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def max_score(nums1, nums2, k)
  n = nums1.length
  idx = (0...n).to_a.sort_by { |i| -nums2[i] }
  pq = MinHeap.new
  s = 0
  ans = 0
  idx.each do |i|
    pq.push(nums1[i])
    s += nums1[i]
    if pq.length > k
      s -= pq.pop
    end
    if pq.length == k
      cand = s * nums2[i]
      ans = cand if cand > ans
    end
  end
  ans
end
