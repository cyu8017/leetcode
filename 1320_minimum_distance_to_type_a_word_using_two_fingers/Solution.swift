// LeetCode 1320 - Minimum Distance to Type a Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

class Solution {
    func minimumDistance(_ word: String) -> Int {
        func distance(_ a: Int, _ b: Int) -> Int {
            if a == 26 { return 0 }
            return abs(a / 6 - b / 6) + abs(a % 6 - b % 6)
        }
        let letters = word.utf8.map { Int($0) - 65 }
        var dp = [26: 0]
        var previous = letters[0]
        for current in letters.dropFirst() {
            var nxt = [Int: Int]()
            for (free, cost) in dp {
                nxt[free] = min(nxt[free, default: Int.max / 4], cost + distance(previous, current))
                nxt[previous] = min(nxt[previous, default: Int.max / 4], cost + distance(free, current))
            }
            dp = nxt
            previous = current
        }
        return dp.values.min() ?? 0
    }
}
