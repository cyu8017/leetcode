# LeetCode 1298 - Maximum Candies You Can Get from Boxes
# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

require "set"

# @param {Integer[]} status
# @param {Integer[]} candies
# @param {Integer[][]} keys
# @param {Integer[][]} contained_boxes
# @param {Integer[]} initial_boxes
# @return {Integer}
def max_candies(status, candies, keys, contained_boxes, initial_boxes)
  owned = Set.new(initial_boxes)
  opened = Set.new
  queue = initial_boxes.select { |box| status[box] == 1 }
  total = 0
  until queue.empty?
    box = queue.shift
    next if opened.include?(box) || status[box] == 0
    opened.add(box)
    total += candies[box]
    keys[box].each do |key|
      status[key] = 1
      queue << key if owned.include?(key) && !opened.include?(key)
    end
    contained_boxes[box].each do |child|
      owned.add(child)
      queue << child if status[child] == 1 && !opened.include?(child)
    end
  end
  total
end
