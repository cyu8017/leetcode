// LeetCode 0274 - H-Index
// https://leetcode.com/problems/h-index/

class Solution {
    func hIndex(_ citations: [Int]) -> Int {
        var buckets = Array(repeating: 0, count: citations.count + 1)
        for citation in citations {
            buckets[min(citation, citations.count)] += 1
        }
        var total = 0
        for h in stride(from: buckets.count - 1, through: 0, by: -1) {
            total += buckets[h]
            if total >= h {
                return h
            }
        }
        return 0
    }
}
