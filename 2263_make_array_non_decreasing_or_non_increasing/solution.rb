# LeetCode 2263 - Make Array Non-decreasing or Non-increasing
# https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

class MaxHeap
  def initialize
    @a = []
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
def convert_array(nums)
  cost = lambda do |arr|
    h = MaxHeap.new
    ans = 0
    arr.each do |x|
      if !h.empty? && h.peek > x
        t = h.pop
        ans += t - x
        h.push(x)
      end
      h.push(x)
    end
    ans
  end
  [cost.call(nums), cost.call(nums.reverse)].min
end

alias solve convert_array
