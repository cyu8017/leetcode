// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/


class Solution {
    func rearrangeString(_ s: String, _ x: Character, _ y: Character) -> String {
        var arr = Array(s)
        var i = 0
        for j in 0..<arr.count {
            if arr[j] == y {
                arr.swapAt(i, j)
                i += 1
            }
        }
        return String(arr)
    }
}
