# LeetCode 3975 - Filter Occupied Intervals
# https://leetcode.com/problems/filter-occupied-intervals/

# @param {Integer[][]} occupied_intervals
# @param {Integer} free_start
# @param {Integer} free_end
# @return {Integer[][]}
def filter_occupied_intervals(occupied_intervals, free_start, free_end)
  occupied_intervals.sort_by! { |a| a[0] }
  busy = [[occupied_intervals[0][0], occupied_intervals[0][1]]]
  (1...occupied_intervals.length).each do |i|
    cur = occupied_intervals[i]
    last = busy[-1]
    if last[1] + 1 < cur[0]
      busy << [cur[0], cur[1]]
    elsif cur[1] > last[1]
      last[1] = cur[1]
    end
  end
  ans = []
  busy.each do |it|
    s, e = it[0], it[1]
    if e < free_start || s > free_end
      ans << [s, e]
    else
      ans << [s, free_start - 1] if s < free_start
      ans << [free_end + 1, e] if e > free_end
    end
  end
  ans
end
