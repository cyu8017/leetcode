// LeetCode 1792 - Maximum Average Pass Ratio
// https://leetcode.com/problems/maximum-average-pass-ratio/

class Solution {
    func maxAverageRatio(_ classes: [[Int]], _ extraStudents: Int) -> Double {
        func gain(_ p: Double, _ t: Double) -> Double {
            return (p + 1) / (t + 1) - p / t
        }

        var heap: [(Double, Double, Double)] = classes.map { cls in
            let p = Double(cls[0])
            let t = Double(cls[1])
            return (gain(p, t), p, t)
        }

        func siftDown(_ start: Int) {
            var i = start
            let n = heap.count
            while true {
                var largest = i
                let l = 2 * i + 1
                let r = 2 * i + 2
                if l < n && heap[l].0 > heap[largest].0 { largest = l }
                if r < n && heap[r].0 > heap[largest].0 { largest = r }
                if largest == i { break }
                heap.swapAt(i, largest)
                i = largest
            }
        }

        for i in stride(from: heap.count / 2 - 1, through: 0, by: -1) {
            siftDown(i)
        }
        for _ in 0..<extraStudents {
            let (_, p, t) = heap[0]
            heap[0] = (gain(p + 1, t + 1), p + 1, t + 1)
            siftDown(0)
        }

        let total = heap.reduce(0.0) { $0 + $1.1 / $1.2 }
        return total / Double(classes.count)
    }
}
