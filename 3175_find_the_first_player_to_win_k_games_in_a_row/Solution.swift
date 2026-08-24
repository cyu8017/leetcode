// LeetCode 3175 - Find The First Player to win K Games in a Row
// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

class Solution {
    func findWinningPlayer(_ skills: [Int], _ k: Int) -> Int {
        let n = skills.count
        let kk = min(k, n - 1)
        var i = 0, cnt = 0
        for j in 1..<n {
            if skills[i] < skills[j] {
                i = j
                cnt = 1
            } else {
                cnt += 1
            }
            if cnt == kk { break }
        }
        return i
    }
}
