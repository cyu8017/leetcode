# LeetCode 1603 - Design Parking System
# https://leetcode.com/problems/design-parking-system/

class ParkingSystem
  def initialize(big, medium, small)
    @spaces = [0, big, medium, small]
  end

  def add_car(car_type)
    return false if @spaces[car_type].zero?

    @spaces[car_type] -= 1
    true
  end
end
