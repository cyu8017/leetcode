// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

class Solution {
    func customSortString(_ order: String, _ s: String) -> String {
        var count = Array(repeating: 0, count: 26)
        let a = Int(Character("a").asciiValue!)
        for ch in s {
            count[Int(ch.asciiValue!) - a] += 1
        }
        var out = ""
        for ch in order {
            let i = Int(ch.asciiValue!) - a
            while count[i] > 0 {
                out.append(ch)
                count[i] -= 1
            }
        }
        for i in 0..<26 {
            while count[i] > 0 {
                out.append(Character(UnicodeScalar(a + i)!))
                count[i] -= 1
            }
        }
        return out
    }
}
