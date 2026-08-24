// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

class Solution {
    func canReorderDoubled(_ arr: [Int]) -> Bool {
        var count = [Int: Int]()
        for x in arr { count[x, default: 0] += 1 }
        let keys = count.keys.sorted { abs($0) < abs($1) }
        for x in keys {
            let need = count[x] ?? 0
            if need == 0 { continue }
            if (count[2 * x] ?? 0) < need { return false }
            count[2 * x]! -= need
        }
        return true
    }
}
