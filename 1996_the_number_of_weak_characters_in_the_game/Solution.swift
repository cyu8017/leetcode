// LeetCode 1996 - The Number of Weak Characters in the Game
// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

class Solution {
    func numberOfWeakCharacters(_ properties: [[Int]]) -> Int {
        var properties = properties.sorted { a, b in
            if a[0] != b[0] { return a[0] < b[0] }
            return a[1] > b[1]
        }
        var ans = 0, maxDef = 0
        for i in stride(from: properties.count - 1, through: 0, by: -1) {
            if properties[i][1] < maxDef {
                ans += 1
            } else {
                maxDef = properties[i][1]
            }
        }
        return ans
    }
}
