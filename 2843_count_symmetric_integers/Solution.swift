// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

class Solution {
    func countSymmetricIntegers(_ low: Int, _ high: Int) -> Int {
        var ans = 0
        for x in low...high {
            let s = Array(String(x))
            if s.count % 2 != 0 { continue }
            let mid = s.count / 2
            var a = 0, b = 0
            for i in 0..<mid {
                a += Int(s[i].asciiValue! - Character("0").asciiValue!)
                b += Int(s[mid + i].asciiValue! - Character("0").asciiValue!)
            }
            if a == b { ans += 1 }
        }
        return ans
    }
}
