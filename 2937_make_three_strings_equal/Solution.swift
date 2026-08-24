// LeetCode 2937 - Make Three Strings Equal
// https://leetcode.com/problems/make-three-strings-equal/

class Solution {
    func findMinimumOperations(_ s1: String, _ s2: String, _ s3: String) -> Int {
        let a = Array(s1), b = Array(s2), c = Array(s3)
        let n = min(a.count, min(b.count, c.count))
        var i = 0
        while i < n && a[i] == b[i] && b[i] == c[i] { i += 1 }
        if i == 0 { return -1 }
        return a.count + b.count + c.count - 3 * i
    }
}
