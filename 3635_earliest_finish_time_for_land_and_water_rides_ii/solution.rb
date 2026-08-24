# LeetCode 3635 - Earliest Finish Time for Land and Water Rides II
# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/

# @param {Integer[]} land_start_time
# @param {Integer[]} land_duration
# @param {Integer[]} water_start_time
# @param {Integer[]} water_duration
# @return {Integer}
def earliest_finish_time(land_start_time, land_duration, water_start_time, water_duration)
  calc = lambda do |a1, t1, a2, t2|
    min_end = (0...a1.length).map { |i| a1[i] + t1[i] }.min
    (0...a2.length).map { |i| [min_end, a2[i]].max + t2[i] }.min
  end
  [
    calc.call(land_start_time, land_duration, water_start_time, water_duration),
    calc.call(water_start_time, water_duration, land_start_time, land_duration)
  ].min
end
