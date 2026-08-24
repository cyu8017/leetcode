# LeetCode 0849 - Maximize Distance to Closest Person
# https://leetcode.com/problems/maximize-distance-to-closest-person/

# @param {Integer[]} seats
# @return {Integer}
def max_dist_to_closest(seats)
  n = seats.length
  prev = -1
  ans = 0
  seats.each_with_index do |occupied, i|
    next if occupied == 0

    ans = prev == -1 ? i : [ans, (i - prev) / 2].max
    prev = i
  end
  [ans, n - 1 - prev].max
end
