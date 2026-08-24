// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

class Solution {
    func smallestString(_ s: String) -> String {
        var arr = Array(s)
        let n = arr.count
        var i = 0
        while i < n && arr[i] == "a" { i += 1 }
        if i == n {
            arr[n - 1] = "z"
            return String(arr)
        }
        while i < n && arr[i] != "a" {
            let v = Int(arr[i].asciiValue!) - 1
            arr[i] = Character(UnicodeScalar(v)!)
            i += 1
        }
        return String(arr)
    }
}
