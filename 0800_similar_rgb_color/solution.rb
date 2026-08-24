# LeetCode 0800 - Similar RGB Color
# https://leetcode.com/problems/similar-rgb-color/

# @param {String} color
# @return {String}
def similar_rgb(color)
  closest = lambda do |component|
    value = component.to_i(16)
    rounded = (value + 8) / 17
    format("%x%x", rounded, rounded)
  end

  "#" + closest.call(color[1, 2]) + closest.call(color[3, 2]) + closest.call(color[5, 2])
end
