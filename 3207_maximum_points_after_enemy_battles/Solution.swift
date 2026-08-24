// LeetCode 3207 - Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/

class Solution {
    func maximumPoints(_ enemyEnergies: [Int], _ currentEnergy: Int) -> Int {
        let e = enemyEnergies.sorted()
        if currentEnergy < e[0] { return 0 }
        var energy = currentEnergy
        var ans = 0
        for i in stride(from: e.count - 1, through: 0, by: -1) {
            ans += energy / e[0]
            energy %= e[0]
            energy += e[i]
        }
        return ans
    }
}
