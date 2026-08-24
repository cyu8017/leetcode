# LeetCode 2126 - Destroying Asteroids
# https://leetcode.com/problems/destroying-asteroids/

# @param {Integer} mass
# @param {Integer[]} asteroids
# @return {Boolean}
def asteroids_destroyed(mass, asteroids)
  cur = mass
  asteroids.sort.each do |a|
    return false if cur < a

    cur += a
  end
  true
end
