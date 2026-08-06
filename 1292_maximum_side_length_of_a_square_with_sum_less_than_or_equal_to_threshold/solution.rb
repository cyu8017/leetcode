# LeetCode 1292 - Maximum Side Length of a Square with Sum Less than or Equal to Threshold
# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

# @param {Integer[][]} mat
# @param {Integer} threshold
# @return {Integer}
def max_side_length(mat, threshold)
  m = mat.length
  n = mat[0].length
  prefix = Array.new(m + 1) { Array.new(n + 1, 0) }
  m.times do |r|
    n.times do |c|
      prefix[r + 1][c + 1] = mat[r][c] + prefix[r][c + 1] + prefix[r + 1][c] - prefix[r][c]
    end
  end
  possible = lambda do |size|
    (size..m).any? do |r|
      (size..n).any? do |c|
        prefix[r][c] - prefix[r - size][c] - prefix[r][c - size] + prefix[r - size][c - size] <= threshold
      end
    end
  end
  lo = 0
  hi = [m, n].min
  while lo < hi
    mid = (lo + hi + 1) / 2
    if possible.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
