# LeetCode 2080 - Range Frequency Queries
# https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery
  def initialize(arr)
    @pos = {}
    arr.each_with_index do |v, i|
      (@pos[v] ||= []) << i
    end
  end

  def query(left, right, value)
    p = @pos[value]
    return 0 if p.nil?

    upper(p, right) - lower(p, left)
  end

  private

  def lower(p, x)
    lo = 0
    hi = p.length
    while lo < hi
      mid = (lo + hi) >> 1
      if p[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end

  def upper(p, x)
    lo = 0
    hi = p.length
    while lo < hi
      mid = (lo + hi) >> 1
      if p[mid] <= x
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
end
