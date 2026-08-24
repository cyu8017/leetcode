// LeetCode 0703 - Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest {
    private var heap = [Int]()
    private let k: Int

    init(_ k: Int, _ nums: [Int]) {
        self.k = k
        for n in nums { add(n) }
    }

    @discardableResult
    func add(_ val: Int) -> Int {
        heapPush(val)
        if heap.count > k { heapPop() }
        return heap[0]
    }

    private func heapPush(_ val: Int) {
        heap.append(val)
        var i = heap.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if heap[p] <= heap[i] { break }
            heap.swapAt(p, i)
            i = p
        }
    }

    private func heapPop() {
        let last = heap.removeLast()
        if heap.isEmpty { return }
        heap[0] = last
        var i = 0
        while true {
            var best = i
            let l = 2 * i + 1, r = 2 * i + 2
            if l < heap.count && heap[l] < heap[best] { best = l }
            if r < heap.count && heap[r] < heap[best] { best = r }
            if best == i { break }
            heap.swapAt(i, best)
            i = best
        }
    }
}
