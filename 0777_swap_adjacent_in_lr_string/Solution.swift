// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

class Solution {
    func canTransform(_ start: String, _ result: String) -> Bool {
        if start.filter({ $0 != "X" }) != result.filter({ $0 != "X" }) { return false }
        let a = Array(start), b = Array(result)
        var i = 0, j = 0, n = a.count
        while i < n && j < n {
            while i < n && a[i] == "X" { i += 1 }
            while j < n && b[j] == "X" { j += 1 }
            if i == n || j == n { break }
            if a[i] != b[j] { return false }
            if a[i] == "L" && i < j { return false }
            if a[i] == "R" && i > j { return false }
            i += 1; j += 1
        }
        return true
    }
}
