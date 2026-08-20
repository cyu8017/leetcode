// LeetCode 1439 - Find the Kth Smallest Sum of a Matrix With Sorted Rows
// https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

class Solution {
    func kthSmallest(_ mat: [[Int]], _ k: Int) -> Int {
        var sums = [0]
        for row in mat {
            var heap = [(sums[0] + row[0], 0, 0)] // value, i, j
            func push(_ t: (Int, Int, Int)) {
                heap.append(t)
                var i = heap.count - 1
                while i > 0 {
                    let p = (i - 1) / 2
                    if heap[p].0 <= heap[i].0 { break }
                    heap.swapAt(p, i); i = p
                }
            }
            func pop() -> (Int, Int, Int) {
                let r = heap[0]
                let last = heap.removeLast()
                if !heap.isEmpty {
                    heap[0] = last
                    var i = 0
                    while true {
                        var s = i
                        let l = 2 * i + 1, rg = 2 * i + 2
                        if l < heap.count && heap[l].0 < heap[s].0 { s = l }
                        if rg < heap.count && heap[rg].0 < heap[s].0 { s = rg }
                        if s == i { break }
                        heap.swapAt(i, s); i = s
                    }
                }
                return r
            }
            var merged = [Int]()
            var seen = Set<[Int]>()
            seen.insert([0, 0])
            while !heap.isEmpty && merged.count < k {
                let (value, i, j) = pop()
                merged.append(value)
                if j + 1 < row.count && !seen.contains([i, j + 1]) {
                    seen.insert([i, j + 1]); push((sums[i] + row[j + 1], i, j + 1))
                }
                if j == 0 && i + 1 < sums.count && !seen.contains([i + 1, 0]) {
                    seen.insert([i + 1, 0]); push((sums[i + 1] + row[0], i + 1, 0))
                }
            }
            sums = merged
        }
        return sums[k - 1]
    }
}
