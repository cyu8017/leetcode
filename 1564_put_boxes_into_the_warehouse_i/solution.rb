# LeetCode 1564 - Put Boxes Into the Warehouse I
# https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

# @param {Integer[]} boxes
# @param {Integer[]} warehouse
# @return {Integer}
def max_boxes_in_warehouse(boxes, warehouse)
  (1...warehouse.length).each do |i|
    warehouse[i] = [warehouse[i], warehouse[i - 1]].min
  end
  boxes = boxes.sort
  room = warehouse.length - 1
  used = 0
  boxes.each do |box|
    room -= 1 while room >= 0 && warehouse[room] < box
    break if room < 0
    used += 1
    room -= 1
  end
  used
end
