# LeetCode 0735 - Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/

# @param {Integer[]} asteroids
# @return {Integer[]}
def asteroid_collision(asteroids)
  stack = []
  asteroids.each do |asteroid|
    exploded = false
    while !stack.empty? && asteroid < 0 && stack[-1] > 0
      if stack[-1] < -asteroid
        stack.pop
        next
      end
      stack.pop if stack[-1] == -asteroid
      exploded = true
      break
    end
    stack << asteroid unless exploded
  end
  stack
end
