# LeetCode 0981 - Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap
  def initialize
    @store = Hash.new { |h, k| h[k] = [] }
  end

  def set(key, value, timestamp)
    @store[key] << [timestamp, value]
    nil
  end

  def get(key, timestamp)
    arr = @store[key]
    return "" if arr.empty?

    lo = 0
    hi = arr.length
    while lo < hi
      mid = (lo + hi) >> 1
      if arr[mid][0] <= timestamp
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo.positive? ? arr[lo - 1][1] : ""
  end
end
