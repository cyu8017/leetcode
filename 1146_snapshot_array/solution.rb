# LeetCode 1146 - Snapshot Array
# https://leetcode.com/problems/snapshot-array/

class SnapshotArray
  def initialize(length)
    @snap_id = 0
    @data = Array.new(length) { [[0, 0]] }
  end

  def set(index, val)
    hist = @data[index]
    if hist[-1][0] == @snap_id
      hist[-1] = [@snap_id, val]
    else
      hist << [@snap_id, val]
    end
  end

  def snap
    @snap_id += 1
    @snap_id - 1
  end

  def get(index, snap_id)
    hist = @data[index]
    lo = 0
    hi = hist.length - 1
    ans = 0
    while lo <= hi
      mid = (lo + hi) / 2
      if hist[mid][0] <= snap_id
        ans = hist[mid][1]
        lo = mid + 1
      else
        hi = mid - 1
      end
    end
    ans
  end
end
