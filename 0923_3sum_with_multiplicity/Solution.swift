// LeetCode 0923 - 3Sum With Multiplicity
// https://leetcode.com/problems/3sum-with-multiplicity/

class Solution {
    func threeSumMulti(_ arr: [Int], _ target: Int) -> Int {
        let mod = 1_000_000_007
        var count = Array(repeating: 0, count: 101)
        for x in arr { count[x] += 1 }
        var ans = 0
        for a in 0...100 where count[a] > 0 {
            for b in a...100 where count[b] > 0 {
                let c = target - a - b
                if c < b || c > 100 || count[c] == 0 { continue }
                if a == b && b == c {
                    ans += count[a] * (count[a] - 1) * (count[a] - 2) / 6
                } else if a == b {
                    ans += count[a] * (count[a] - 1) / 2 * count[c]
                } else if b == c {
                    ans += count[a] * count[b] * (count[b] - 1) / 2
                } else {
                    ans += count[a] * count[b] * count[c]
                }
            }
        }
        return ans % mod
    }
}
