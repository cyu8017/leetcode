// LeetCode 3664 - Two-Letter Card Game
// https://leetcode.com/problems/two-letter-card-game/

class Solution {
    func pairGroup(_ arr: [Int]) -> [Int] {
        var total = 0, mx = 0
        for i in 0..<26 {
            total += arr[i]
            mx = max(mx, arr[i])
        }
        var pairs = total / 2
        if total - mx < pairs { pairs = total - mx }
        return [pairs, total - 2 * pairs]
    }

    func score(_ cards: [String], _ x: Character) -> Int {
        var xx = 0
        var left = Array(repeating: 0, count: 26)
        var right = Array(repeating: 0, count: 26)
        for c in cards {
            let a = c.first!, b = c.last!
            if a == x && b == x { xx += 1 }
            else if a == x { left[Int(b.asciiValue! - 97)] += 1 }
            else if b == x { right[Int(a.asciiValue! - 97)] += 1 }
        }
        let lp = pairGroup(left), rp = pairGroup(right)
        var ans = lp[0] + rp[0]
        let rem = lp[1] + rp[1]
        let use = min(xx, rem)
        ans += use
        xx -= use
        ans += xx / 2
        return ans
    }
}
