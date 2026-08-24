// LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

class Solution {
    func maximumLength(_ s: String) -> Int {
        let chars = Array(s)
        var groups = Array(repeating: [Int](), count: 26)
        let n = chars.count
        var i = 0
        let aVal = Int(Character("a").asciiValue!)
        while i < n {
            var j = i
            while j < n && chars[j] == chars[i] { j += 1 }
            groups[Int(chars[i].asciiValue!) - aVal].append(j - i)
            i = j
        }
        var ans = -1
        for c in 0..<26 {
            var arr = groups[c]
            if arr.isEmpty { continue }
            arr.sort(by: >)
            for L in stride(from: arr[0], through: 1, by: -1) {
                var cnt = 0
                for g in arr where g >= L { cnt += g - L + 1 }
                if cnt >= 3 {
                    ans = max(ans, L)
                    break
                }
            }
        }
        return ans
    }
}
