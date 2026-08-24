// LeetCode 2462 - Total Cost to Hire K Workers
// https://leetcode.com/problems/total-cost-to-hire-k-workers/

class Solution {
    func totalCost(_ costs: [Int], _ k: Int, _ candidates: Int) -> Int {
        var leftH = MinHeap< (Int, Int) > { a, b in a.0 != b.0 ? a.0 < b.0 : a.1 < b.1 }
        var rightH = MinHeap< (Int, Int) > { a, b in a.0 != b.0 ? a.0 < b.0 : a.1 < b.1 }
        let n = costs.count
        var l = 0, r = n - 1
        while l <= r && leftH.count < candidates {
            leftH.push((costs[l], l))
            l += 1
        }
        while r >= l && rightH.count < candidates {
            rightH.push((costs[r], r))
            r -= 1
        }
        var ans = 0
        for _ in 0..<k {
            var useLeft = false
            if !leftH.isEmpty && !rightH.isEmpty {
                let lt = leftH.peek()!, rt = rightH.peek()!
                if lt.0 < rt.0 || (lt.0 == rt.0 && lt.1 <= rt.1) { useLeft = true }
            } else if !leftH.isEmpty {
                useLeft = true
            }
            if useLeft {
                ans += leftH.pop().0
                if l <= r {
                    leftH.push((costs[l], l))
                    l += 1
                }
            } else {
                ans += rightH.pop().0
                if l <= r {
                    rightH.push((costs[r], r))
                    r -= 1
                }
            }
        }
        return ans
    }

    private struct MinHeap<T> {
        var data = [T]()
        let less: (T, T) -> Bool
        init(_ less: @escaping (T, T) -> Bool) { self.less = less }
        var isEmpty: Bool { data.isEmpty }
        var count: Int { data.count }
        func peek() -> T? { data.first }
        mutating func push(_ x: T) {
            data.append(x)
            var i = data.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if !less(data[i], data[p]) { break }
                data.swapAt(i, p)
                i = p
            }
        }
        mutating func pop() -> T {
            let res = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                var i = 0
                while true {
                    var smallest = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < data.count && less(data[l], data[smallest]) { smallest = l }
                    if r < data.count && less(data[r], data[smallest]) { smallest = r }
                    if smallest == i { break }
                    data.swapAt(i, smallest)
                    i = smallest
                }
            }
            return res
        }
    }

}
