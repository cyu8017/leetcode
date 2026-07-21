# LeetCode 1854 - Maximum Population Year
# https://leetcode.com/problems/maximum-population-year/

# @param {Integer[][]} logs
# @return {Integer}
def maximum_population(logs)
  diff = Array.new(101, 0)
  logs.each do |birth, death|
    diff[birth - 1950] += 1
    diff[death - 1950] -= 1
  end

  best_year = 1950
  best_population = 0
  population = 0

  (0...101).each do |offset|
    population += diff[offset]
    if population > best_population
      best_population = population
      best_year = 1950 + offset
    end
  end

  best_year
end
