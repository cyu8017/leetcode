// LeetCode 1989 - Maximum Number of People That Can Be Caught in Tag
// https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/

class Solution {
    func catchMaximumAmountofPeople(_ team: [Int], _ dist: Int) -> Int {
        var ans = 0, j = 0
        let n = team.count
        for (i, x) in team.enumerated() where x == 1 {
            while j < n && (team[j] == 1 || i - j > dist) { j += 1 }
            if j < n && abs(i - j) <= dist {
                ans += 1
                j += 1
            }
        }
        return ans
    }
}
