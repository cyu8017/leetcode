# LeetCode 0853 - Car Fleet
# https://leetcode.com/problems/car-fleet/

# @param {Integer} target
# @param {Integer[]} position
# @param {Integer[]} speed
# @return {Integer}
def car_fleet(target, position, speed)
  cars = position.zip(speed).sort.reverse
  fleets = 0
  max_time = 0.0
  cars.each do |pos, spd|
    time = (target - pos).to_f / spd
    if time > max_time
      fleets += 1
      max_time = time
    end
  end
  fleets
end
