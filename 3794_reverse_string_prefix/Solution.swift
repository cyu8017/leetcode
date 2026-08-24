// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

class Solution {
    func reversePrefix(_ s: String, _ k: Int) -> String {
        var arr = Array(s)
        var i = 0, j = k - 1
        while i < j {
            arr.swapAt(i, j)
            i += 1
            j -= 1
        }
        return String(arr)
    }
}
