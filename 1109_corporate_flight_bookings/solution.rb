# LeetCode 1109 - Corporate Flight Bookings
# https://leetcode.com/problems/corporate-flight-bookings/

# @param {Integer[][]} bookings
# @param {Integer} n
# @return {Integer[]}
def corp_flight_bookings(bookings, n)
  diff = Array.new(n + 1, 0)
  bookings.each do |first, last, seats|
    diff[first - 1] += seats
    diff[last] -= seats
  end
  ans = []
  cur = 0
  n.times do |i|
    cur += diff[i]
    ans << cur
  end
  ans
end
