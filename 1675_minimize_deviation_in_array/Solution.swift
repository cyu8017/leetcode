// LeetCode 1675 - Minimize Deviation in Array
// https://leetcode.com/problems/minimize-deviation-in-array/

class Solution {
    func minimumDeviation(_ nums: [Int]) -> Int {
        var heap = [Int]()
        func push(_ x: Int) {
            heap.append(x)
            var i = heap.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if heap[p] >= heap[i] { break }
                heap.swapAt(p, i)
                i = p
            }
        }
        func pop() -> Int {
            let top = heap[0]
            let last = heap.removeLast()
            if heap.isEmpty { return top }
            heap[0] = last
            var i = 0
            let n = heap.count
            while true {
                var largest = i
                let l = 2 * i + 1, r = 2 * i + 2
                if l < n && heap[l] > heap[largest] { largest = l }
                if r < n && heap[r] > heap[largest] { largest = r }
                if largest == i { break }
                heap.swapAt(i, largest)
                i = largest
            }
            return top
        }
        var mn = Int.max
        for var x in nums {
            if x % 2 == 1 { x *= 2 }
            mn = min(mn, x)
            push(x)
        }
        var ans = Int.max
        while true {
            let x = pop()
            ans = min(ans, x - mn)
            if x % 2 == 1 { return ans }
            let nx = x / 2
            mn = min(mn, nx)
            push(nx)
        }
    }
}
