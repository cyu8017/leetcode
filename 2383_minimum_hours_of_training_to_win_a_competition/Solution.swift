// LeetCode 2383 - Minimum Hours of Training to Win a Competition
// https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

class Solution {
    func minNumberOfHours(_ initialEnergy: Int, _ initialExperience: Int, _ energy: [Int], _ experience: [Int]) -> Int {
        var ans = 0, en = initialEnergy, ex = initialExperience
        for i in 0..<energy.count {
            if en <= energy[i] {
                let need = energy[i] - en + 1
                ans += need
                en += need
            }
            if ex <= experience[i] {
                let need = experience[i] - ex + 1
                ans += need
                ex += need
            }
            en -= energy[i]
            ex += experience[i]
        }
        return ans
    }
}
