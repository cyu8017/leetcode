# LeetCode 1046 - Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/

# @param {Integer[]} stones
# @return {Integer}
def last_stone_weight(stones)
  heap = stones.dup
  while heap.length > 1
    heap.sort!
    a = heap.pop
    b = heap.pop
    heap << (a - b) if a != b
  end
  heap.empty? ? 0 : heap[0]
end
