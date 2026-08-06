# LeetCode 1962 - Remove Stones to Minimize the Total
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

# @param {Integer[]} piles
# @param {Integer} k
# @return {Integer}
def min_stone_sum(piles, k)
  heap = piles.map { |p| -p }
  (heap.length / 2 - 1).downto(0) { |i| sift_down(heap, i) }
  k.times do
    x = -heap[0]
    heap[0] = -(x - x / 2)
    sift_down(heap, 0)
  end
  -heap.sum
end

def sift_down(heap, i)
  n = heap.length
  loop do
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = l if l < n && heap[l] < heap[smallest]
    smallest = r if r < n && heap[r] < heap[smallest]
    break if smallest == i
    heap[i], heap[smallest] = heap[smallest], heap[i]
    i = smallest
  end
end
