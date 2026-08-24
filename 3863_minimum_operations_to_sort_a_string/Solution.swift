// LeetCode 3863 - Minimum Operations To Sort A String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/

class Solution {
    func minOperations(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var sorted = true
        if n > 1 {
            for i in 1..<n {
                if chars[i] < chars[i - 1] { sorted = false; break }
            }
        }
        if sorted { return 0 }
        if n == 2 { return -1 }
        var mn = chars[0], mx = chars[0]
        for c in chars {
            if c < mn { mn = c }
            if c > mx { mx = c }
        }
        if chars[0] == mn || chars[n - 1] == mx { return 1 }
        if n > 2 {
            for i in 1..<(n - 1) {
                if chars[i] == mn || chars[i] == mx { return 2 }
            }
        }
        return 3
    }
}
