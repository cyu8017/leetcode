// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution {
    func largestGoodInteger(_ num: String) -> String {
        let arr = Array(num)
        var best = ""
        if arr.count >= 3 {
            for i in 0..<(arr.count - 2) {
                if arr[i] == arr[i + 1] && arr[i] == arr[i + 2] {
                    let cand = String(arr[i...i + 2])
                    if cand > best { best = cand }
                }
            }
        }
        return best
    }
}
