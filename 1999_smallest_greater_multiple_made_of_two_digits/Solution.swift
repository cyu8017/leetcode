// LeetCode 1999 - Smallest Greater Multiple Made of Two Digits
// https://leetcode.com/problems/smallest-greater-multiple-made-of-two-digits/

class Solution {
    func findInteger(_ k: Int, _ digit1: Int, _ digit2: Int) -> Int {
        let digits = Array(Set([digit1, digit2])).sorted()
        var q: [Int] = []
        var head = 0
        var seen = Set<Int>()
        for d in digits where d != 0 {
            q.append(d)
            seen.insert(d)
        }
        if q.isEmpty { return -1 }
        let limit = Int(Int32.max)
        while head < q.count {
            let x = q[head]; head += 1
            if x > k && x % k == 0 { return x }
            for d in digits {
                let nx = x * 10 + d
                if nx <= limit && !seen.contains(nx) {
                    seen.insert(nx)
                    q.append(nx)
                }
            }
        }
        return -1
    }
}
