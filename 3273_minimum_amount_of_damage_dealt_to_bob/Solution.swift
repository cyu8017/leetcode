// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

class Solution {
    func minDamage(_ power: Int, _ damage: [Int], _ health: [Int]) -> Int {
        let n = damage.count
        var arr: [(Int, Int)] = []
        var totalDmg = 0
        for i in 0..<n {
            let hits = (health[i] + power - 1) / power
            arr.append((damage[i], hits))
            totalDmg += damage[i]
        }
        arr.sort { a, b in a.1 * b.0 < b.1 * a.0 }
        var ans = 0, cur = totalDmg
        for e in arr {
            ans += cur * e.1
            cur -= e.0
        }
        return ans
    }
}
