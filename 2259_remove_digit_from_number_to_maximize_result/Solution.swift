// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution {
    func removeDigit(_ number: String, _ digit: Character) -> String {
        var best = ""
        let arr = Array(number)
        for i in 0..<arr.count where arr[i] == digit {
            let cand = String(arr[0..<i] + arr[(i + 1)...])
            if cand > best { best = cand }
        }
        return best
    }
}
