// LeetCode 3823 - Reverse Letters Then Special Characters In A String
// https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

class Solution {
    func reverseByType(_ s: String) -> String {
        var a = [Character]()
        var b = [Character]()
        for c in s {
            if c.isLetter { a.append(c) } else { b.append(c) }
        }
        var j = a.count, k = b.count
        var arr = Array(s)
        for i in 0..<arr.count {
            if arr[i].isLetter {
                j -= 1
                arr[i] = a[j]
            } else {
                k -= 1
                arr[i] = b[k]
            }
        }
        return String(arr)
    }
}
