
# @param {Integer} n
# @param {Integer} index
# @param {Integer} max_sum
# @return {Integer}
def max_value(n, index, max_sum)
  min_side_sum = lambda do |value, count|
    if value > count
      (value - 1 + value - count) * count / 2
    else
      value * (value - 1) / 2 + (count - value + 1)
    end
  end

  lo = 1
  hi = max_sum
  while lo < hi
    mid = (lo + hi + 1) / 2
    total = min_side_sum.call(mid, index) + mid + min_side_sum.call(mid, n - index - 1)
    if total <= max_sum
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
