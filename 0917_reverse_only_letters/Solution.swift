// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

class Solution {
    func reverseOnlyLetters(_ s: String) -> String {
        var arr = Array(s)
        var i = 0, j = arr.count - 1
        while i < j {
            while i < j && !arr[i].isLetter { i += 1 }
            while i < j && !arr[j].isLetter { j -= 1 }
            arr.swapAt(i, j)
            i += 1
            j -= 1
        }
        return String(arr)
    }
}
