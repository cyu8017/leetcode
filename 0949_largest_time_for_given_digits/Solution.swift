// LeetCode 0949 - Largest Time for Given Digits
// https://leetcode.com/problems/largest-time-for-given-digits/

class Solution {
    func largestTimeFromDigits(_ arr: [Int]) -> String {
        var a = arr.sorted()
        var best = ""
        func nextPermutation(_ a: inout [Int]) -> Bool {
            var i = a.count - 2
            while i >= 0 && a[i] >= a[i + 1] { i -= 1 }
            if i < 0 { return false }
            var j = a.count - 1
            while a[j] <= a[i] { j -= 1 }
            a.swapAt(i, j)
            var l = i + 1, r = a.count - 1
            while l < r { a.swapAt(l, r); l += 1; r -= 1 }
            return true
        }
        repeat {
            let hours = 10 * a[0] + a[1]
            let minutes = 10 * a[2] + a[3]
            if hours < 24 && minutes < 60 {
                let cand = String(format: "%02d:%02d", hours, minutes)
                if cand > best { best = cand }
            }
        } while nextPermutation(&a)
        return best
    }
}
