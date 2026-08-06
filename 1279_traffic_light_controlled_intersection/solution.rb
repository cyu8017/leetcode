# LeetCode 1279 - Traffic Light Controlled Intersection
# https://leetcode.com/problems/traffic-light-controlled-intersection/

class TrafficLight
  def initialize
    @green_road = 1
    @mutex = Mutex.new
  end

  def car_arrived(car_id, road_id, direction, turn_green, cross_car)
    @mutex.synchronize do
      if road_id != @green_road
        turn_green.call
        @green_road = road_id
      end
      cross_car.call
    end
  end
end
