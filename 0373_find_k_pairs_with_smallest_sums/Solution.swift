// LeetCode 0373 - Find K Pairs with Smallest Sums
// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution {
    func kSmallestPairs(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> [[Int]] {
        if nums1.isEmpty || nums2.isEmpty || k == 0 {
            return []
        }

        var heap: [(Int, Int, Int)] = []
        let limit = min(nums1.count, k)
        for index in 0..<limit {
            heapPush(&heap, (nums1[index] + nums2[0], index, 0))
        }

        var result: [[Int]] = []
        while !heap.isEmpty && result.count < k {
            let (_, index1, index2) = heapPop(&heap)
            result.append([nums1[index1], nums2[index2]])
            if index2 + 1 < nums2.count {
                heapPush(&heap, (nums1[index1] + nums2[index2 + 1], index1, index2 + 1))
            }
        }

        return result
    }

    private func heapPush(_ heap: inout [(Int, Int, Int)], _ item: (Int, Int, Int)) {
        heap.append(item)
        var index = heap.count - 1
        while index > 0 {
            let parent = (index - 1) / 2
            if heap[parent].0 <= heap[index].0 {
                break
            }
            heap.swapAt(parent, index)
            index = parent
        }
    }

    private func heapPop(_ heap: inout [(Int, Int, Int)]) -> (Int, Int, Int) {
        let top = heap[0]
        let last = heap.removeLast()
        if heap.isEmpty {
            return top
        }
        heap[0] = last
        var index = 0
        while true {
            var smallest = index
            let left = index * 2 + 1
            let right = index * 2 + 2
            if left < heap.count && heap[left].0 < heap[smallest].0 {
                smallest = left
            }
            if right < heap.count && heap[right].0 < heap[smallest].0 {
                smallest = right
            }
            if smallest == index {
                break
            }
            heap.swapAt(smallest, index)
            index = smallest
        }
        return top
    }
}
