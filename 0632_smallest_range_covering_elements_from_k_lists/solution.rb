# LeetCode 0632 - Smallest Range Covering Elements from K Lists
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

# @param {Integer[][]} nums
# @return {Integer[]}
def smallest_range(nums)
  heap = []
  current_max = -Float::INFINITY

  nums.each_with_index do |arr, i|
    heap << [arr[0], i, 0]
    current_max = [current_max, arr[0]].max
  end
  heap.sort!

  best_left = heap[0][0]
  best_right = current_max

  loop do
    value, list_index, index = heap.shift
    if current_max - value < best_right - best_left
      best_left = value
      best_right = current_max
    end
    break if index + 1 == nums[list_index].length

    nxt = nums[list_index][index + 1]
    heap << [nxt, list_index, index + 1]
    heap.sort!
    current_max = [current_max, nxt].max
  end

  [best_left, best_right]
end
