// LeetCode 1962 - Remove Stones to Minimize the Total
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution {
    func minStoneSum(_ piles: [Int], _ k: Int) -> Int {
        var heap = piles
        // max-heap via negate-less-than with manual heap
        func siftUp(_ i0: Int) {
            var i = i0
            while i > 0 {
                let p = (i - 1) / 2
                if heap[p] >= heap[i] { break }
                heap.swapAt(p, i); i = p
            }
        }
        func siftDown(_ i0: Int) {
            var i = i0
            while true {
                var largest = i
                let l = 2 * i + 1, r = 2 * i + 2
                if l < heap.count && heap[l] > heap[largest] { largest = l }
                if r < heap.count && heap[r] > heap[largest] { largest = r }
                if largest == i { break }
                heap.swapAt(i, largest); i = largest
            }
        }
        for i in stride(from: heap.count / 2 - 1, through: 0, by: -1) { siftDown(i) }
        for _ in 0..<k {
            let x = heap[0]
            heap[0] = x - x / 2
            siftDown(0)
        }
        return heap.reduce(0, +)
    }
}
