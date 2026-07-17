# LeetCode 1776 - Car Fleet II
# https://leetcode.com/problems/car-fleet-ii/

# @param {Integer[][]} cars
# @return {Float[]}
def get_collision_times(cars)
  n = cars.length
  ans = Array.new(n, -1.0)
  stack = []
  (n - 1).downto(0) do |i|
    pos, speed = cars[i]
    until stack.empty?
      j = stack.last
      if speed <= cars[j][1]
        stack.pop
        next
      end
      t = (cars[j][0] - pos).to_f / (speed - cars[j][1])
      if ans[j] < 0 || t <= ans[j]
        ans[i] = t
        break
      end
      stack.pop
    end
    stack << i
  end
  ans
end
