// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

class Solution {
    func kthCharacter(_ k: Int, _ operations: [Int]) -> Character {
        var k = k
        var shift = 0
        var ops = operations
        while !ops.isEmpty {
            let op = ops.removeLast()
            let half = 1 << ops.count
            if k > half {
                k -= half
                if op == 1 { shift += 1 }
            }
        }
        return Character(UnicodeScalar(97 + shift % 26)!)
    }
}
