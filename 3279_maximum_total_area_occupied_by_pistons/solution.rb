# LeetCode 3279 - Maximum Total Area Occupied by Pistons
# https://leetcode.com/problems/maximum-total-area-occupied-by-pistons/

# @param {Integer} height
# @param {Integer[]} positions
# @param {String} directions
# @return {Integer}
def max_area(height, positions, directions)
  n = positions.length
  pos = positions.dup
  dirc = directions.chars
  best = 0
  (0..(2 * height)).each do |_t|
    s = pos.sum
    best = s if s > best
    (0...n).each do |i|
      if dirc[i] == "U"
        if pos[i] == height
          dirc[i] = "D"
          pos[i] -= 1
        else
          pos[i] += 1
        end
      elsif pos[i] == 0
        dirc[i] = "U"
        pos[i] += 1
      else
        pos[i] -= 1
      end
    end
  end
  best
end
