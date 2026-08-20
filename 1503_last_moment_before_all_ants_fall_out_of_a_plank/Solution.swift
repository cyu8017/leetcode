// LeetCode 1503 - Last Moment Before All Ants Fall Out of a Plank
// https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/

class Solution {
    func getLastMoment(_ n: Int, _ left: [Int], _ right: [Int]) -> Int {
        let leftMax = left.max() ?? 0
        let rightMin = right.min() ?? n
        return max(leftMax, n - rightMin)
    }
}
