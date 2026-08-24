// LeetCode 2739 - Total Distance Traveled
// https://leetcode.com/problems/total-distance-traveled/

class Solution {
    func distanceTraveled(_ mainTank: Int, _ additionalTank: Int) -> Int {
        var mainTank = mainTank, additionalTank = additionalTank, ans = 0
        while mainTank > 0 {
            if mainTank >= 5 {
                ans += 50
                mainTank -= 5
                if additionalTank > 0 {
                    additionalTank -= 1
                    mainTank += 1
                }
            } else {
                ans += mainTank * 10
                mainTank = 0
            }
        }
        return ans
    }
}
