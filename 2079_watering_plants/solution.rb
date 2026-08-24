# LeetCode 2079 - Watering Plants
# https://leetcode.com/problems/watering-plants/

# @param {Integer[]} plants
# @param {Integer} capacity
# @return {Integer}
def watering_plants(plants, capacity)
  ans = 0
  cur = capacity
  plants.each_with_index do |p, i|
    if cur < p
      ans += i * 2
      cur = capacity
    end
    cur -= p
    ans += 1
  end
  ans
end
