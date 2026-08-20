// LeetCode 1953 - Maximum Number of Weeks for Which You Can Work
// https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

class Solution {
    func numberOfWeeks(_ milestones: [Int]) -> Int {
        let total = milestones.reduce(0, +)
        let mx = milestones.max()!
        let rest = total - mx
        if mx > rest + 1 { return 2 * rest + 1 }
        return total
    }
}
