# LeetCode 3323 - Minimize Connected Groups by Inserting Interval
# https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

# @param {Integer[][]} intervals
# @param {Integer} k
# @return {Integer}
def min_connected_groups(intervals, k)
  intervals.sort_by! { |a| a[0] }
  merged = []
  intervals.each do |it|
    if merged.empty? || it[0] > merged[-1][1]
      merged << [it[0], it[1]]
    elsif it[1] > merged[-1][1]
      merged[-1][1] = it[1]
    end
  end
  m = merged.length
  ans = m
  m.times do |i|
    endv = merged[i][1] + k
    j = i
    j += 1 while j < m && merged[j][0] <= endv
    groups = i + 1 + (m - j)
    ans = groups if groups < ans
  end
  ans
end
