# LeetCode 2147 - Number of Ways to Divide a Long Corridor
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

# @param {String} corridor
# @return {Integer}
def number_of_ways(corridor)
  mod = 1_000_000_007
  seats = []
  corridor.chars.each_with_index { |ch, i| seats << i if ch == "S" }
  return 0 if seats.empty? || seats.length.odd?

  ans = 1
  2.step(seats.length - 1, 2) { |i| ans = ans * (seats[i] - seats[i - 1]) % mod }
  ans
end
