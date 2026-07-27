// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution {
    func minimumEffort(_ tasks: [[Int]]) -> Int {
        let tasks = tasks.sorted { ($0[1] - $0[0]) > ($1[1] - $1[0]) }
        var energy = 0, spent = 0
        for t in tasks {
            energy = max(energy, spent + t[1])
            spent += t[0]
        }
        return energy
    }
}
