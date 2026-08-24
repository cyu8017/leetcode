// LeetCode 2383 - Minimum Hours of Training to Win a Competition
// https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/

class Solution {
    fun minNumberOfHours(initialEnergy: Int, initialExperience: Int, energy: IntArray, experience: IntArray): Int {
        var ans = 0
        var en = initialEnergy
        var ex = initialExperience
        for (i in energy.indices) {
            if (en <= energy[i]) {
                val need = energy[i] - en + 1
                ans += need
                en += need
            }
            if (ex <= experience[i]) {
                val need = experience[i] - ex + 1
                ans += need
                ex += need
            }
            en -= energy[i]
            ex += experience[i]
        }
        return ans
    }
}
