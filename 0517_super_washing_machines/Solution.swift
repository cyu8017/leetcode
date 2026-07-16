// LeetCode 0517 - Super Washing Machines
// https://leetcode.com/problems/super-washing-machines/

class Solution {
    func findMinMoves(_ machines: [Int]) -> Int {
        let total = machines.reduce(0, +)
        let count = machines.count
        if total % count != 0 {
            return -1
        }

        let target = total / count
        var prefix = 0
        var result = 0

        for clothes in machines {
            let diff = clothes - target
            prefix += diff
            result = max(result, abs(prefix), diff)
        }

        return result
    }
}
