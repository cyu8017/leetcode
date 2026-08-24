// LeetCode 2182 - Construct String With Repeat Limit
// https://leetcode.com/problems/construct-string-with-repeat-limit/

class Solution {
    func repeatLimitedString(_ s: String, _ repeatLimit: Int) -> String {
        var freq = [Int](repeating: 0, count: 26)
        for c in s { freq[Int(c.asciiValue! - 97)] += 1 }
        var ans = [Character]()
        while true {
            var placed = false
            for c in stride(from: 25, through: 0, by: -1) {
                if freq[c] == 0 { continue }
                if !ans.isEmpty && Int(ans.last!.asciiValue! - 97) == c {
                    var found = false
                    for d in stride(from: c - 1, through: 0, by: -1) where freq[d] > 0 {
                        ans.append(Character(UnicodeScalar(97 + d)!))
                        freq[d] -= 1
                        found = true
                        placed = true
                        break
                    }
                    if !found { return String(ans) }
                    break
                }
                let use = min(freq[c], repeatLimit)
                for _ in 0..<use { ans.append(Character(UnicodeScalar(97 + c)!)) }
                freq[c] -= use
                placed = true
                break
            }
            if !placed { break }
        }
        return String(ans)
    }
}
