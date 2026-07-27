# LeetCode 1642 - Furthest Building You Can Reach
# https://leetcode.com/problems/furthest-building-you-can-reach/

class MinHeap1642
  def initialize
    @a = []
  end

  def length
    @a.length
  end

  def push(x)
    @a << x
    i = @a.length - 1
    while i.positive?
      p = (i - 1) / 2
      break if @a[p] <= @a[i]

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
      r = l + 1
      smallest = i
      smallest = l if l < @a.length && @a[l] < @a[smallest]
      smallest = r if r < @a.length && @a[r] < @a[smallest]
      break if smallest == i

      @a[i], @a[smallest] = @a[smallest], @a[i]
      i = smallest
    end
    top
  end
end

# @param {Integer[]} heights
# @param {Integer} bricks
# @param {Integer} ladders
# @return {Integer}
def furthest_building(heights, bricks, ladders)
  climbs = MinHeap1642.new
  (0...(heights.length - 1)).each do |i|
    d = heights[i + 1] - heights[i]
    next if d <= 0

    climbs.push(d)
    bricks -= climbs.pop if climbs.length > ladders
    return i if bricks.negative?
  end
  heights.length - 1
end
