# LeetCode 2437 - Number of Valid Clock Times
# https://leetcode.com/problems/number-of-valid-clock-times/

# @param {String} time
# @return {Integer}
def count_time(time)
  ans = 0
  (0...24).each do |h|
    (0...60).each do |m|
      h0 = (h / 10).to_s
      h1 = (h % 10).to_s
      m0 = (m / 10).to_s
      m1 = (m % 10).to_s
      next if time[0] != "?" && time[0] != h0
      next if time[1] != "?" && time[1] != h1
      next if time[3] != "?" && time[3] != m0
      next if time[4] != "?" && time[4] != m1

      ans += 1
    end
  end
  ans
end
