// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

class Solution {
    func sumDistance(_ nums: [Int], _ s: String, _ d: Int) -> Int {
        let MOD = 1_000_000_007
        let chars = Array(s)
        var pos = zip(nums, chars).map { $0 + ($1 == "R" ? d : -d) }
        pos.sort()
        var ans = 0
        var pref = 0
        for i in pos.indices {
            ans = (ans + pos[i] * i - pref) % MOD
            pref += pos[i]
        }
        return (ans % MOD + MOD) % MOD
    }
}
