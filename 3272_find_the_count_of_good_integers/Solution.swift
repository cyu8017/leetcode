// LeetCode 3272 - Find the Count of Good Integers
// https://leetcode.com/problems/find-the-count-of-good-integers/

class Solution {
    func countGoodIntegers(_ n: Int, _ k: Int) -> Int {
        var start = 1
        let half = (n + 1) / 2
        for _ in 1..<half { start *= 10 }
        let end = start * 10
        var seen = Set<String>()
        var ans = 0
        var fact = Array(repeating: 1, count: n + 1)
        for i in 1...n { fact[i] = fact[i - 1] * i }
        for h in start..<end {
            let s = String(h)
            var pal = s
            let sc = Array(s)
            var revStart = sc.count - 1
            if n % 2 == 1 { revStart -= 1 }
            if revStart >= 0 {
                for i in stride(from: revStart, through: 0, by: -1) { pal.append(sc[i]) }
            }
            if Int(pal)! % k != 0 { continue }
            let key = String(pal.sorted())
            if !seen.insert(key).inserted { continue }
            var cnt = Array(repeating: 0, count: 10)
            for c in pal { cnt[Int(c.asciiValue! - Character("0").asciiValue!)] += 1 }
            var total = fact[n]
            for c in cnt { total /= fact[c] }
            if cnt[0] > 0 {
                var bad = fact[n - 1]
                cnt[0] -= 1
                for c in cnt { bad /= fact[c] }
                cnt[0] += 1
                total -= bad
            }
            ans += total
        }
        return ans
    }
}
