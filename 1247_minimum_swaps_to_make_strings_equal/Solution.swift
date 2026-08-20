// LeetCode 1247 - Minimum Swaps to Make Strings Equal
// https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/

class Solution {
    func minimumSwap(_ s1: String, _ s2: String) -> Int {
        let a = Array(s1), b = Array(s2)
        var xy = 0, yx = 0
        for i in 0..<a.count {
            if a[i] == "x" && b[i] == "y" { xy += 1 }
            if a[i] == "y" && b[i] == "x" { yx += 1 }
        }
        if (xy + yx) % 2 != 0 { return -1 }
        return xy / 2 + yx / 2 + (xy % 2) * 2
    }
}
