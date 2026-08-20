// LeetCode 1540 - Can Convert String in K Moves
// https://leetcode.com/problems/can-convert-string-in-k-moves/

class Solution {
    func canConvertString(_ s: String, _ t: String, _ k: Int) -> Bool {
        let a = Array(s), b = Array(t)
        if a.count != b.count { return false }
        var used = Array(repeating: 0, count: 26)
        for i in 0..<a.count {
            let shift = (Int(b[i].asciiValue!) - Int(a[i].asciiValue!) + 26) % 26
            if shift == 0 { continue }
            used[shift] += 1
            if shift + 26 * (used[shift] - 1) > k { return false }
        }
        return true
    }
}
