# LeetCode 1580 - Put Boxes Into the Warehouse II
# https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

# @param {Integer[]} boxes
# @param {Integer[]} warehouse
# @return {Integer}
def max_boxes_in_warehouse(boxes, warehouse)
  n = warehouse.length
  left = warehouse.dup
  right = warehouse.dup
  (1...n).each { |i| left[i] = [left[i], left[i - 1]].min }
  (n - 2).downto(0) { |i| right[i] = [right[i], right[i + 1]].min }
  capacity = (0...n).map { |i| [left[i], right[i]].max }.sort
  boxes = boxes.sort
  i = 0
  capacity.each do |room|
    if i < boxes.length && boxes[i] <= room
      i += 1
    end
  end
  i
end
