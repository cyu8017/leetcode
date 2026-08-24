# LeetCode 3102 - Minimize Manhattan Distances
# https://leetcode.com/problems/minimize-manhattan-distances/

class MultiSet
  def initialize
    @m = Hash.new(0)
    @keys = []
  end

  def merge(x, v)
    nv = @m[x] + v
    if nv == 0
      @m.delete(x)
      i = bisect_left(@keys, x)
      @keys.delete_at(i) if i < @keys.length && @keys[i] == x
    else
      if !@m.key?(x) || @m[x] == 0
        i = bisect_left(@keys, x)
        @keys.insert(i, x) unless i < @keys.length && @keys[i] == x
      end
      @m[x] = nv
    end
  end

  def first
    @keys[0]
  end

  def last
    @keys[-1]
  end

  def bisect_left(a, x)
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) / 2
      if a[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
end

# @param {Integer[][]} points
# @return {Integer}
def minimum_distance(points)
  st1 = MultiSet.new
  st2 = MultiSet.new
  points.each do |p|
    st1.merge(p[0] + p[1], 1)
    st2.merge(p[0] - p[1], 1)
  end
  ans = 10**18
  points.each do |p|
    x = p[0]
    y = p[1]
    st1.merge(x + y, -1)
    st2.merge(x - y, -1)
    ans = [ans, [st1.last - st1.first, st2.last - st2.first].max].min
    st1.merge(x + y, 1)
    st2.merge(x - y, 1)
  end
  ans
end
