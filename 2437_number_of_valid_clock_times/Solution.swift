// LeetCode 2437 - Number of Valid Clock Times
// https://leetcode.com/problems/number-of-valid-clock-times/

class Solution {
    func countTime(_ time: String) -> Int {
        let t = Array(time)
        var ans = 0
        for h in 0..<24 {
            for m in 0..<60 {
                let h0 = Character(String(h / 10))
                let h1 = Character(String(h % 10))
                let m0 = Character(String(m / 10))
                let m1 = Character(String(m % 10))
                if t[0] != "?" && t[0] != h0 { continue }
                if t[1] != "?" && t[1] != h1 { continue }
                if t[3] != "?" && t[3] != m0 { continue }
                if t[4] != "?" && t[4] != m1 { continue }
                ans += 1
            }
        }
        return ans
    }
}
