// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution {
    func minMaxDifference(_ num: Int) -> Int {
        let s = Array(String(num))
        func remap(_ from: Character, _ to: Character) -> Int {
            var v = 0
            for c in s {
                let d = c == from ? to : c
                v = v * 10 + Int(String(d))!
            }
            return v
        }
        var maxV = num
        for c in s where c != "9" {
            maxV = remap(c, "9")
            break
        }
        let minV = remap(s[0], "0")
        return maxV - minV
    }
}
