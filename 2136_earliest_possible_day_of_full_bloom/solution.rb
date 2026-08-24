# LeetCode 2136 - Earliest Possible Day of Full Bloom
# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

# @param {Integer[]} plant_time
# @param {Integer[]} grow_time
# @return {Integer}
def earliest_full_bloom(plant_time, grow_time)
  n = plant_time.length
  idx = (0...n).to_a
  idx.sort_by! { |a| -grow_time[a] }
  day = 0
  ans = 0
  idx.each do |i|
    day += plant_time[i]
    ans = [ans, day + grow_time[i]].max
  end
  ans
end
