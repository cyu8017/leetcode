# LeetCode 2105 - Watering Plants II
# https://leetcode.com/problems/watering-plants-ii/

# @param {Integer[]} plants
# @param {Integer} capacity_a
# @param {Integer} capacity_b
# @return {Integer}
def minimum_refill(plants, capacity_a, capacity_b)
  i = 0
  j = plants.length - 1
  a = capacity_a
  b = capacity_b
  ans = 0
  while i < j
    if a < plants[i]
      ans += 1
      a = capacity_a
    end
    a -= plants[i]
    i += 1
    if b < plants[j]
      ans += 1
      b = capacity_b
    end
    b -= plants[j]
    j -= 1
  end
  if i == j
    if a >= b
      ans += 1 if a < plants[i]
    elsif b < plants[i]
      ans += 1
    end
  end
  ans
end
