// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution {
    func digitCount(_ num: String) -> Bool {
        let arr = Array(num)
        var cnt = [Int](repeating: 0, count: 10)
        for c in arr { cnt[Int(String(c))!] += 1 }
        for i in 0..<arr.count {
            if cnt[i] != Int(String(arr[i]))! { return false }
        }
        return true
    }
}
