// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

class Solution {
    func getSmallestString(_ s: String) -> String {
        var arr = Array(s)
        for i in 1..<arr.count {
            let a = arr[i - 1], b = arr[i]
            if a > b && (Int(a.asciiValue!) % 2) == (Int(b.asciiValue!) % 2) {
                arr.swapAt(i - 1, i)
                return String(arr)
            }
        }
        return s
    }
}
