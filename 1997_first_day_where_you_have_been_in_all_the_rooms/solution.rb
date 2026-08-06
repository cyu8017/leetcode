# LeetCode 1997 - First Day Where You Have Been in All the Rooms
# https://leetcode.com/problems/first-day-where-you-have-been-in-all-the-rooms/

# @param {Integer[]} next_visit
# @return {Integer}
def first_day_been_in_all_rooms(next_visit)
  mod = 10**9 + 7
  n = next_visit.length
  dp = Array.new(n, 0)
  (1...n).each do |i|
    dp[i] = (2 * dp[i - 1] - dp[next_visit[i - 1]] + 2) % mod
  end
  dp[n - 1]
end
