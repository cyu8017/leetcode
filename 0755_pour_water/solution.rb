# LeetCode 0755 - Pour Water
# https://leetcode.com/problems/pour-water/

# @param {Integer[]} heights
# @param {Integer} volume
# @param {Integer} k
# @return {Integer[]}
def pour_water(heights, volume, k)
  volume.times do
    index = k
    (k - 1).downto(0) do |i|
      break if heights[i] > heights[index]

      index = i if heights[i] < heights[index]
    end
    if index != k
      heights[index] += 1
      next
    end

    index = k
    ((k + 1)...heights.length).each do |i|
      break if heights[i] > heights[index]

      index = i if heights[i] < heights[index]
    end
    heights[index] += 1
  end
  heights
end
