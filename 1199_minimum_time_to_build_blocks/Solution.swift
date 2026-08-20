// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

class Solution {
    func minBuildTime(_ blocks: [Int], _ split: Int) -> Int {
        var heap = blocks.sorted()
        while heap.count > 1 {
            heap.removeFirst()
            let b = heap.removeFirst()
            let merged = b + split
            let idx = heap.firstIndex { $0 >= merged } ?? heap.count
            heap.insert(merged, at: idx)
        }
        return heap[0]
    }
}
