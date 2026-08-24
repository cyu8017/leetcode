# LeetCode 2188 - Minimum Time to Finish the Race
# https://leetcode.com/problems/minimum-time-to-finish-the-race/

# @param {Integer[][]} tires
# @param {Integer} change_time
# @param {Integer} num_laps
# @return {Integer}
def minimum_finish_time(tires, change_time, num_laps)
  inf = 1 << 30
  min_time = Array.new(20, inf)
  tires.each do |f, r|
    t = f
    lap = f
    x = 1
    while x < 20
      min_time[x] = t if t < min_time[x]
      lap *= r
      break if lap > change_time + f

      t += lap
      x += 1
    end
  end
  dp = Array.new(num_laps + 1, inf)
  dp[0] = -change_time
  (1..num_laps).each do |i|
    j = 1
    while j <= i && j < 20
      dp[i] = [dp[i], dp[i - j] + change_time + min_time[j]].min
      j += 1
    end
  end
  dp[num_laps]
end
