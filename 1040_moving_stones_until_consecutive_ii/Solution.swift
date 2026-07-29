// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

class Solution {
    func numMovesStonesII(_ stones: [Int]) -> [Int] {
        let stones = stones.sorted()
        let n = stones.count
        let maxMoves = max(stones[n - 1] - stones[1] - n + 2, stones[n - 2] - stones[0] - n + 2)
        var minMoves = maxMoves
        var i = 0
        for j in 0..<n {
            while stones[j] - stones[i] + 1 > n { i += 1 }
            let inside = j - i + 1
            if inside == n - 1 && stones[j] - stones[i] + 1 == n - 1 {
                minMoves = min(minMoves, 2)
            } else {
                minMoves = min(minMoves, n - inside)
            }
        }
        return [minMoves, maxMoves]
    }
}
