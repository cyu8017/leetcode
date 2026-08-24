// LeetCode 2059 - Minimum Operations to Convert Number
// https://leetcode.com/problems/minimum-operations-to-convert-number/

class Solution {
    func minimumOperations(_ nums: [Int], _ start: Int, _ goal: Int) -> Int {
        if start == goal { return 0 }
        var vis = Set<Int>([start])
        var q = [start]
        var head = 0
        var steps = 0
        while head < q.count {
            steps += 1
            let sz = q.count - head
            for _ in 0..<sz {
                let cur = q[head]
                head += 1
                for x in nums {
                    for nxt in [cur + x, cur - x, cur ^ x] {
                        if nxt == goal { return steps }
                        if nxt >= 0 && nxt <= 1000 && vis.insert(nxt).inserted {
                            q.append(nxt)
                        }
                    }
                }
            }
        }
        return -1
    }
}
