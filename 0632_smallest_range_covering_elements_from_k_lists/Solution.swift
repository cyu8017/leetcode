// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

class Solution {
    func smallestRange(_ nums: [[Int]]) -> [Int] {
        var heap = [[Int]]()
        var currentMax = Int.min
        for i in 0..<nums.count {
            let val = nums[i][0]
            heapPush(&heap, [val, i, 0])
            currentMax = max(currentMax, val)
        }
        var bestLeft = heap[0][0]
        var bestRight = currentMax
        while true {
            let top = heapPop(&heap)
            let value = top[0]
            let listIndex = top[1]
            let index = top[2]
            if currentMax - value < bestRight - bestLeft {
                bestLeft = value
                bestRight = currentMax
            }
            if index + 1 == nums[listIndex].count { break }
            let nxt = nums[listIndex][index + 1]
            heapPush(&heap, [nxt, listIndex, index + 1])
            currentMax = max(currentMax, nxt)
        }
        return [bestLeft, bestRight]
    }

    private func heapPush(_ heap: inout [[Int]], _ val: [Int]) {
        heap.append(val)
        var i = heap.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if heap[p][0] <= heap[i][0] { break }
            heap.swapAt(p, i)
            i = p
        }
    }

    private func heapPop(_ heap: inout [[Int]]) -> [Int] {
        let top = heap[0]
        let last = heap.removeLast()
        if !heap.isEmpty {
            heap[0] = last
            var i = 0
            while true {
                var best = i
                let l = 2 * i + 1, r = 2 * i + 2
                if l < heap.count && heap[l][0] < heap[best][0] { best = l }
                if r < heap.count && heap[r][0] < heap[best][0] { best = r }
                if best == i { break }
                heap.swapAt(i, best)
                i = best
            }
        }
        return top
    }

}
