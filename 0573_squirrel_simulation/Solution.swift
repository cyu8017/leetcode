// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

class Solution {
    func minDistance(_ height: Int, _ width: Int, _ tree: [Int], _ squirrel: [Int], _ nuts: [[Int]]) -> Int {
        var total = 0
        var bestSave = Int.min
        for nut in nuts {
            let treeDist = abs(tree[0] - nut[0]) + abs(tree[1] - nut[1])
            let squirrelDist = abs(squirrel[0] - nut[0]) + abs(squirrel[1] - nut[1])
            total += 2 * treeDist
            bestSave = max(bestSave, treeDist - squirrelDist)
        }
        return total - bestSave
    }
}
