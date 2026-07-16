// LeetCode 0403 - Frog Jump
// https://leetcode.com/problems/frog-jump/

class Solution {
    func canCross(_ stones: [Int]) -> Bool {
        let stoneSet = Set(stones)
        var jumps = Dictionary(uniqueKeysWithValues: stones.map { ($0, Set<Int>()) })
        jumps[0, default: []].insert(0)

        for stone in stones {
            for jump in jumps[stone, default: []] {
                for nextJump in [jump - 1, jump, jump + 1] where nextJump > 0 {
                    if stoneSet.contains(stone + nextJump) {
                        jumps[stone + nextJump, default: []].insert(nextJump)
                    }
                }
            }
        }

        return !(jumps[stones.last!, default: []].isEmpty)
    }
}
