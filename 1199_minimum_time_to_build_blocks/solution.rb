# LeetCode 1199 - Minimum Time to Build Blocks
# https://leetcode.com/problems/minimum-time-to-build-blocks/

# @param {Integer[]} blocks
# @param {Integer} split
# @return {Integer}
def min_build_time(blocks, split)
  heap = blocks.sort
  while heap.length > 1
    heap.shift
    cost = heap.shift + split
    idx = heap.bsearch_index { |x| x >= cost } || heap.length
    heap.insert(idx, cost)
  end
  heap[0]
end
