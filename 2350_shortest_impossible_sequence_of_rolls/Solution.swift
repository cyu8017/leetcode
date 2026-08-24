// LeetCode 2350 - Shortest Impossible Sequence of Rolls
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/

class Solution {
    func shortestSequence(_ rolls: [Int], _ k: Int) -> Int {
        var seen = Set<Int>()
        var ans = 1
        for r in rolls {
            seen.insert(r)
            if seen.count == k {
                ans += 1
                seen.removeAll()
            }
        }
        return ans
    }
}
