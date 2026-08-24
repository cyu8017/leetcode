# LeetCode 0668 - Kth Smallest Number in Multiplication Table
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

# @param {Integer} m
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def find_kth_number(m, n, k)
  count_le = lambda do |x|
    (1..m).sum { |row| [x / row, n].min }
  end

  lo = 1
  hi = m * n
  while lo < hi
    mid = (lo + hi) / 2
    if count_le.call(mid) >= k
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
