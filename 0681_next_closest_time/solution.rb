# LeetCode 0681 - Next Closest Time
# https://leetcode.com/problems/next-closest-time/

# @param {String} time
# @return {String}
def next_closest_time(time)
  digits = {}
  (time[0, 2] + time[3, 2]).each_char { |ch| digits[ch] = true }
  start = time[0, 2].to_i * 60 + time[3, 2].to_i
  (1..(24 * 60)).each do |delta|
    mins = (start + delta) % (24 * 60)
    hh, mm = mins.divmod(60)
    candidate = format("%02d%02d", hh, mm)
    if candidate.chars.all? { |ch| digits[ch] }
      return format("%02d:%02d", hh, mm)
    end
  end
  time
end
