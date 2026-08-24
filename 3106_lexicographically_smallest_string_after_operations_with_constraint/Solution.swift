// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

class Solution {
    func getSmallestString(_ s: String, _ k: Int) -> String {
        var arr = Array(s)
        var rem = k
        let aVal = Character("a").asciiValue!
        for i in 0..<arr.count {
            let c1 = arr[i]
            var c2 = aVal
            while c2 < c1.asciiValue! {
                let d1 = Int(c1.asciiValue! - c2)
                let d = min(d1, 26 - d1)
                if d <= rem {
                    arr[i] = Character(UnicodeScalar(c2))
                    rem -= d
                    break
                }
                c2 += 1
            }
        }
        return String(arr)
    }
}
