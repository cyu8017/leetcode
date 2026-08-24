// LeetCode 2243 - Calculate Digit Sum of a String
// https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution {
    func digitSum(_ s: String, _ k: Int) -> String {
        var s = s
        while s.count > k {
            var next = ""
            let arr = Array(s)
            var i = 0
            while i < arr.count {
                var sum = 0
                let end = min(i + k, arr.count)
                for j in i..<end { sum += Int(String(arr[j]))! }
                next += String(sum)
                i += k
            }
            s = next
        }
        return s
    }
}
