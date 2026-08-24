// LeetCode 2029 - Stone Game IX
// https://leetcode.com/problems/stone-game-ix/

class Solution {
    func stoneGameIX(_ stones: [Int]) -> Bool {
        var cnt = [Int](repeating: 0, count: 3)
        for s in stones { cnt[s % 3] += 1 }
        if cnt[0] % 2 == 0 { return cnt[1] > 0 && cnt[2] > 0 }
        return abs(cnt[1] - cnt[2]) > 2
    }
}
