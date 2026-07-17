# LeetCode 1732 - Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/

# @param {Integer[]} gain
# @return {Integer}
def largest_altitude(gain)
  altitude = 0
  best = 0
  gain.each do |change|
    altitude += change
    best = altitude if altitude > best
  end
  best
end
