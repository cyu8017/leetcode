# LeetCode 0568 - Maximum Vacation Days
# https://leetcode.com/problems/maximum-vacation-days/

# @param {Integer[][]} flights
# @param {Integer[][]} days
# @return {Integer}
def max_vacation_days(flights, days)
  cities = flights.length
  weeks = days[0].length
  neg = -10**9

  dp = Array.new(cities, neg)
  dp[0] = 0

  weeks.times do |week|
    nxt = Array.new(cities, neg)
    cities.times do |city|
      next if dp[city] == neg

      cities.times do |dest|
        if dest == city || flights[city][dest] != 0
          nxt[dest] = [nxt[dest], dp[city] + days[dest][week]].max
        end
      end
    end
    dp = nxt
  end

  dp.max
end
