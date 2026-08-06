# LeetCode 1344 - Angle Between Hands Of A Clock
# https://leetcode.com/problems/angle-between-hands-of-a-clock/

def angle_clock(hour, minutes)
  difference = ((hour % 12) * 30 + minutes * 0.5 - minutes * 6).abs
  [difference, 360 - difference].min
end
