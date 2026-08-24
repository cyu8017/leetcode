# LeetCode 0949 - Largest Time for Given Digits
# https://leetcode.com/problems/largest-time-for-given-digits/

# @param {Integer[]} arr
# @return {String}
def largest_time_from_digits(arr)
  best = ""
  arr.permutation.each do |a, b, c, d|
    hours = 10 * a + b
    minutes = 10 * c + d
    next unless hours < 24 && minutes < 60

    cand = format("%02d:%02d", hours, minutes)
    best = cand if cand > best
  end
  best
end
