# LeetCode 3986 - Number of Elapsed Seconds Between Two Times
# https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

# @param {String} start_time
# @param {String} end_time
# @return {Integer}
def seconds_between_times(start_time, end_time)
  to_seconds = lambda do |s|
    h = (s[0].ord - 48) * 10 + (s[1].ord - 48)
    m = (s[3].ord - 48) * 10 + (s[4].ord - 48)
    sec = (s[6].ord - 48) * 10 + (s[7].ord - 48)
    h * 3600 + m * 60 + sec
  end
  to_seconds.call(end_time) - to_seconds.call(start_time)
end
