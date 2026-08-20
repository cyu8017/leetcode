// LeetCode 1363 - Largest Multiple of Three
// https://leetcode.com/problems/largest-multiple-of-three/

class Solution {
    func largestMultipleOfThree(_ digits: [Int]) -> String {
        var cnt = Array(repeating: 0, count: 10)
        for d in digits { cnt[d] += 1 }
        let rem = digits.reduce(0, +) % 3
        func remove(_ r: Int, _ k: Int) -> Bool {
            var k = k
            var d = r
            while d < 10 {
                while cnt[d] > 0 && k > 0 { cnt[d] -= 1; k -= 1 }
                if k == 0 { return true }
                d += 3
            }
            return false
        }
        if rem != 0 && !remove(rem, 1) { _ = remove(3 - rem, 2) }
        var s = ""
        for d in stride(from: 9, through: 0, by: -1) {
            s += String(repeating: Character(UnicodeScalar(48 + d)!), count: cnt[d])
        }
        if s.isEmpty { return "" }
        if s.first == "0" { return "0" }
        return s
    }
}
