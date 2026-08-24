// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

class Solution {
    func checkStrings(_ s1: String, _ s2: String) -> Bool {
        var even1 = Array(repeating: 0, count: 26)
        var odd1 = Array(repeating: 0, count: 26)
        var even2 = Array(repeating: 0, count: 26)
        var odd2 = Array(repeating: 0, count: 26)
        let a = Array(s1), b = Array(s2)
        for i in 0..<a.count {
            let i1 = Int(a[i].asciiValue! - Character("a").asciiValue!)
            let i2 = Int(b[i].asciiValue! - Character("a").asciiValue!)
            if i % 2 == 0 {
                even1[i1] += 1
                even2[i2] += 1
            } else {
                odd1[i1] += 1
                odd2[i2] += 1
            }
        }
        return even1 == even2 && odd1 == odd2
    }
}
