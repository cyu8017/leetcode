# LeetCode 0373 - Find K Pairs with Smallest Sums
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution
  def k_smallest_pairs(nums1, nums2, k)
    return [] if nums1.empty? || nums2.empty? || k.zero?

    heap = []
    limit = [nums1.length, k].min
    limit.times do |index|
      heap_push(heap, [nums1[index] + nums2[0], index, 0])
    end

    result = []
    while !heap.empty? && result.length < k
      _, index1, index2 = heap_pop(heap)
      result << [nums1[index1], nums2[index2]]
      if index2 + 1 < nums2.length
        heap_push(heap, [nums1[index1] + nums2[index2 + 1], index1, index2 + 1])
      end
    end

    result
  end

  alias_method :kSmallestPairs, :k_smallest_pairs

  private

  def heap_push(heap, item)
    heap << item
    index = heap.length - 1
    while index > 0
      parent = (index - 1) / 2
      break if heap[parent][0] <= heap[index][0]

      heap[parent], heap[index] = heap[index], heap[parent]
      index = parent
    end
  end

  def heap_pop(heap)
    top = heap[0]
    last = heap.pop
    return top if heap.empty?

    heap[0] = last
    index = 0
    loop do
      smallest = index
      left = index * 2 + 1
      right = index * 2 + 2
      smallest = left if left < heap.length && heap[left][0] < heap[smallest][0]
      smallest = right if right < heap.length && heap[right][0] < heap[smallest][0]
      break if smallest == index

      heap[smallest], heap[index] = heap[index], heap[smallest]
      index = smallest
    end
    top
  end
end
