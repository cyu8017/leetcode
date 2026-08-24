# LeetCode 0871 - Minimum Number of Refueling Stops
# https://leetcode.com/problems/minimum-number-of-refueling-stops/

class MaxHeap
  def initialize
    @a = []
  end

  def empty?
    @a.empty?
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

# @param {Integer} target
# @param {Integer} start_fuel
# @param {Integer[][]} stations
# @return {Integer}
def min_refuel_stops(target, start_fuel, stations)
  pq = MaxHeap.new
  stations = stations + [[target, 0]]
  ans = 0
  prev = 0
  fuel = start_fuel
  stations.each do |pos, gas|
    fuel -= pos - prev
    while !pq.empty? && fuel < 0
      fuel += pq.pop
      ans += 1
    end
    return -1 if fuel < 0

    pq.push(gas)
    prev = pos
  end
  ans
end
