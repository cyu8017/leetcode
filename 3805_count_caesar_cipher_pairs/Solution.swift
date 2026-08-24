// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

class Solution {
    func countPairs(_ words: [String]) -> Int {
        var cnt = [String: Int]()
        for word in words {
            var s = Array(word)
            let k = Int(Character("z").asciiValue! - s[0].asciiValue!)
            if s.count > 1 {
                for i in 1..<s.count {
                    let v = Int(s[i].asciiValue! - 97)
                    s[i] = Character(UnicodeScalar(97 + (v + k) % 26)!)
                }
            }
            s[0] = "z"
            let key = String(s)
            cnt[key, default: 0] += 1
        }
        var ans = 0
        for v in cnt.values { ans += v * (v - 1) / 2 }
        return ans
    }
}
