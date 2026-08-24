# LeetCode 3394 - Check if Grid can be Cut into Sections
# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

# @param {Integer[][]} rects
# @param {Integer} axis
# @return {Boolean}
def check_cut(rects, axis)
  arr = rects.map { |r| axis == 0 ? [r[0], r[2]] : [r[1], r[3]] }
  arr.sort_by! { |x| [x[0], x[1]] }
  cuts = 0
  ending = arr[0][1]
  (1...arr.length).each do |i|
    if arr[i][0] >= ending
      cuts += 1
      ending = arr[i][1]
      return true if cuts >= 2
    elsif arr[i][1] > ending
      ending = arr[i][1]
    end
  end
  false
end

# @param {Integer} n
# @param {Integer[][]} rectangles
# @return {Boolean}
def check_valid_cuts(n, rectangles)
  check_cut(rectangles, 0) || check_cut(rectangles, 1)
end
