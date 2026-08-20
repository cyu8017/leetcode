// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

class Solution {
    func isPossibleDivide(_ nums: [Int], _ k: Int) -> Bool {
        if nums.count % k != 0 { return false }
        var count: [Int: Int] = [:]
        for x in nums { count[x, default: 0] += 1 }
        let keys = count.keys.sorted()
        for x in keys {
            let c = count[x]!
            if c == 0 { continue }
            for i in 0..<k {
                let v = count[x + i, default: 0]
                if v < c { return false }
                count[x + i] = v - c
            }
        }
        return true
    }
}
