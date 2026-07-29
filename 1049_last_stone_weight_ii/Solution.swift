// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/

class Solution {
    func lastStoneWeightII(_ stones: [Int]) -> Int {
        let total = stones.reduce(0, +)
        var reachable: Set<Int> = [0]
        for stone in stones {
            var next = reachable
            for s in reachable { next.insert(s + stone) }
            reachable = next
        }
        var best = total
        for s in reachable {
            best = min(best, abs(total - 2 * s))
        }
        return best
    }
}
