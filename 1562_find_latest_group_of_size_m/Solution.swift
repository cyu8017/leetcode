// LeetCode 1562 - Find Latest Group of Size M
// https://leetcode.com/problems/find-latest-group-of-size-m/

class Solution {
    func findLatestStep(_ arr: [Int], _ m: Int) -> Int {
        if m == arr.count { return m }
        var lengths = [Int: Int]()
        var answer = -1
        for (step, x) in arr.enumerated() {
            let left = lengths[x - 1, default: 0]
            let right = lengths[x + 1, default: 0]
            let size = left + 1 + right
            lengths[x - left] = size
            lengths[x + right] = size
            if left == m || right == m { answer = step }
        }
        return answer
    }
}
