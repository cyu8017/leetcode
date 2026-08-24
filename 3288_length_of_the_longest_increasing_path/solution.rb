# LeetCode 3288 - Length of the Longest Increasing Path
# https://leetcode.com/problems/length-of-the-longest-increasing-path/

# @param {Integer[]} a
# @return {Integer}
def lis(a)
  tails = []
  a.each do |x|
    lo = 0
    hi = tails.length
    while lo < hi
      mid = (lo + hi) >> 1
      if tails[mid] < x
        lo = mid + 1
      else
        hi = mid
      end
    end
    if lo == tails.length
      tails << x
    else
      tails[lo] = x
    end
  end
  tails.length
end

# @param {Integer[][]} coordinates
# @param {Integer} k
# @return {Integer}
def max_path_length(coordinates, k)
  n = coordinates.length
  arr = n.times.map { |i| [coordinates[i][0], coordinates[i][1], i] }
  arr.sort_by! { |a| [a[0], -a[1]] }
  kx = coordinates[k][0]
  ky = coordinates[k][1]
  left = []
  right = []
  arr.each do |p|
    left << p[1] if p[0] < kx && p[1] < ky
    right << p[1] if p[0] > kx && p[1] > ky
  end
  lis(left) + 1 + lis(right)
end
