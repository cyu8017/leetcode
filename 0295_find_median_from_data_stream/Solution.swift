// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder {
    private var small: [Int] = []
    private var large: [Int] = []

    init() {
    }

    func addNum(_ num: Int) {
        push(&small, -num, isMaxHeap: true)
        push(&large, -pop(&small, isMaxHeap: true), isMaxHeap: false)
        if large.count > small.count {
            push(&small, -pop(&large, isMaxHeap: false), isMaxHeap: true)
        }
    }

    func findMedian() -> Double {
        if small.count > large.count {
            return Double(-small[0])
        }
        return Double(-small[0] + large[0]) / 2.0
    }

    private func push(_ heap: inout [Int], _ value: Int, isMaxHeap: Bool) {
        heap.append(value)
        bubbleUp(&heap, heap.count - 1, isMaxHeap: isMaxHeap)
    }

    private func pop(_ heap: inout [Int], isMaxHeap: Bool) -> Int {
        let top = heap[0]
        let last = heap.removeLast()
        if !heap.isEmpty {
            heap[0] = last
            bubbleDown(&heap, 0, isMaxHeap: isMaxHeap)
        }
        return top
    }

    private func bubbleUp(_ heap: inout [Int], _ index: Int, isMaxHeap: Bool) {
        var current = index
        while current > 0 {
            let parent = (current - 1) / 2
            if isMaxHeap ? heap[current] <= heap[parent] : heap[current] >= heap[parent] {
                break
            }
            heap.swapAt(current, parent)
            current = parent
        }
    }

    private func bubbleDown(_ heap: inout [Int], _ index: Int, isMaxHeap: Bool) {
        var current = index
        while true {
            var target = current
            let left = current * 2 + 1
            let right = left + 1
            if left < heap.count && (isMaxHeap ? heap[left] > heap[target] : heap[left] < heap[target]) {
                target = left
            }
            if right < heap.count && (isMaxHeap ? heap[right] > heap[target] : heap[right] < heap[target]) {
                target = right
            }
            if target == current {
                break
            }
            heap.swapAt(current, target)
            current = target
        }
    }
}
