// LeetCode 1046 - Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/

class Solution {
    func lastStoneWeight(_ stones: [Int]) -> Int {
        var stones = stones
        while stones.count > 1 {
            stones.sort(by: >)
            let a = stones.removeFirst()
            let b = stones.removeFirst()
            if a != b { stones.append(a - b) }
        }
        return stones.first ?? 0
    }
}
