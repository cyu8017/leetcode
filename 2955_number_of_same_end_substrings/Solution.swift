// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

class Solution {
    func sameEndSubstringCount(_ s: String, _ queries: [[Int]]) -> [Int] {
        let chars = Array(s)
        let n = chars.count
        var pref = Array(repeating: Array(repeating: 0, count: 26), count: n + 1)
        let aVal = Int(Character("a").asciiValue!)
        for i in 0..<n {
            pref[i + 1] = pref[i]
            pref[i + 1][Int(chars[i].asciiValue!) - aVal] += 1
        }
        var ans = Array(repeating: 0, count: queries.count)
        for qi in 0..<queries.count {
            let l = queries[qi][0], r = queries[qi][1]
            var total = 0
            for c in 0..<26 {
                let cnt = pref[r + 1][c] - pref[l][c]
                total += cnt * (cnt + 1) / 2
            }
            ans[qi] = total
        }
        return ans
    }
}
