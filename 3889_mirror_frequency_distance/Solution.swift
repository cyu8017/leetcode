// LeetCode 3889 - Mirror Frequency Distance
// https://leetcode.com/problems/mirror-frequency-distance/

class Solution {
    func mirrorFrequency(_ s: String) -> Int {
        var freq = [Character: Int]()
        for c in s { freq[c, default: 0] += 1 }
        var ans = 0
        var vis = [Character: Bool]()
        for (c, v) in freq {
            let m: Character
            if c >= "a" && c <= "z" {
                m = Character(UnicodeScalar(97 + 25 - Int(c.asciiValue! - 97))!)
            } else {
                m = Character(UnicodeScalar(48 + (9 - Int(c.asciiValue! - 48)))!)
            }
            if vis[m] == true { continue }
            vis[c] = true
            let mv = freq[m, default: 0]
            ans += abs(v - mv)
        }
        return ans
    }
}
