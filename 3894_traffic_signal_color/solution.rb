# LeetCode 3894 - Traffic Signal Color
# https://leetcode.com/problems/traffic-signal-color/

# @param {Integer} timer
# @return {String}
def traffic_signal(timer)
  return "Green" if timer == 0
  return "Orange" if timer == 30
  return "Red" if timer > 30 && timer <= 90
  "Invalid"
end
