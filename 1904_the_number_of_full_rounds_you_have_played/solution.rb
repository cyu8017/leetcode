# LeetCode 1904 - The Number of Full Rounds You Have Played
# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

# @param {String} login_time
# @param {String} logout_time
# @return {Integer}
def number_of_rounds(login_time, logout_time)
  to_min = lambda do |t|
    h, m = t.split(":").map(&:to_i)
    h * 60 + m
  end
  start = to_min.call(login_time)
  end_t = to_min.call(logout_time)
  end_t += 24 * 60 if end_t < start
  start = (start + 14) / 15 * 15
  end_t = end_t / 15 * 15
  [0, (end_t - start) / 15].max
end
