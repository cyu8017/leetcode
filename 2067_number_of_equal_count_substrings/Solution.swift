// LeetCode 2067 - Number of Equal Count Substrings
// https://leetcode.com/problems/number-of-equal-count-substrings/

class Solution {
    func equalCountSubstrings(_ s: String, _ count: Int) -> Int {
        let chars = Array(s)
        let n = chars.count
        var seen = [Bool](repeating: false, count: 26)
        var maxUnique = 0
        for c in chars {
            let i = Int(c.asciiValue! - 97)
            if !seen[i] { seen[i] = true; maxUnique += 1 }
        }
        var ans = 0
        for u in 1...maxUnique {
            let needLen = u * count
            if needLen > n { break }
            var freq = [Int](repeating: 0, count: 26)
            var have = 0
            for i in 0..<n {
                let c = Int(chars[i].asciiValue! - 97)
                freq[c] += 1
                if freq[c] == count { have += 1 }
                else if freq[c] == count + 1 { have -= 1 }
                if i >= needLen {
                    let p = Int(chars[i - needLen].asciiValue! - 97)
                    if freq[p] == count { have -= 1 }
                    else if freq[p] == count + 1 { have += 1 }
                    freq[p] -= 1
                }
                if i + 1 >= needLen && have == u { ans += 1 }
            }
        }
        return ans
    }
}
