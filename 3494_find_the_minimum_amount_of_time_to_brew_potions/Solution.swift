// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

class Solution {
    func minTime(_ skill: [Int], _ mana: [Int]) -> Int {
        let n = skill.count, m = mana.count
        var done = Array(repeating: 0, count: n)
        for j in 0..<m {
            var t = 0
            for i in 0..<n {
                if done[i] > t { t = done[i] }
                t += skill[i] * mana[j]
                done[i] = t
            }
            for i in stride(from: n - 2, through: 0, by: -1) {
                done[i] = done[i + 1] - skill[i + 1] * mana[j]
            }
        }
        return done[n - 1]
    }
}
