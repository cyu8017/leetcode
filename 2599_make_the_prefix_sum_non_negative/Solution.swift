// LeetCode 2599 - Make the Prefix Sum Non-negative
// https://leetcode.com/problems/make-the-prefix-sum-non-negative/

class Solution {
    func makePrefSumNonNegative(_ nums: [Int]) -> Int {
        var h = Heap<Int> { $0 < $1 }
        var sum = 0, ans = 0
        for x in nums {
            sum += x
            if x < 0 { h.push(x) }
            if sum < 0 {
                let worst = h.pop()
                sum -= worst
                ans += 1
            }
        }
        return ans
    }

    private struct Heap<T> {
        var data = [T]()
        let less: (T, T) -> Bool
        init(_ less: @escaping (T, T) -> Bool) { self.less = less }
        var isEmpty: Bool { data.isEmpty }
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
