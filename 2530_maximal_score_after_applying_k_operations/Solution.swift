// LeetCode 2530 - Maximal Score After Applying K Operations
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

class Solution {
    func maxKelements(_ nums: [Int], _ k: Int) -> Int {
        var pq = Heap<Int> { $0 > $1 }
        for x in nums { pq.push(x) }
        var ans = 0
        for _ in 0..<k {
            let x = pq.pop()
            ans += x
            pq.push((x + 2) / 3)
        }
        return ans
    }

    private struct Heap<T> {
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
                data.swapAt(i, p); i = p
            }
        }
        mutating func pop() -> T {
            let res = data[0]
            let last = data.removeLast()
            if !data.isEmpty {
                data[0] = last
                var i = 0
                while true {
                    var s = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < data.count && less(data[l], data[s]) { s = l }
                    if r < data.count && less(data[r], data[s]) { s = r }
                    if s == i { break }
                    data.swapAt(i, s); i = s
                }
            }
            return res
        }
    }

}
