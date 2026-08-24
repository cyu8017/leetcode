// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

class Solution {
    func largestPalindrome(_ n: Int, _ k: Int) -> String {
        var digits = Array(repeating: Character("9"), count: n)
        let half = (n + 1) / 2
        switch k {
        case 1, 3, 9:
            return String(digits)
        case 2:
            digits[0] = "8"; digits[n - 1] = "8"
            return String(digits)
        case 4:
            if n == 1 { return "8" }
            digits[0] = "8"; digits[1] = "8"; digits[n - 1] = "8"; digits[n - 2] = "8"
            return String(digits)
        case 5:
            digits[0] = "5"; digits[n - 1] = "5"
            return String(digits)
        case 8:
            if n <= 2 { return String(repeating: "8", count: n) }
            digits[0] = "8"; digits[1] = "8"; digits[2] = "8"
            digits[n - 1] = "8"; digits[n - 2] = "8"; digits[n - 3] = "8"
            return String(digits)
        case 6:
            if n == 1 { return "6" }
            digits[0] = "8"; digits[n - 1] = "8"
            let sum = 16 + 9 * (n - 2)
            let need = sum % 3
            if need != 0 {
                let pos = half - 1
                let v = Int(digits[pos].asciiValue! - Character("0").asciiValue!) - need
                digits[pos] = Character(UnicodeScalar(UInt8(Character("0").asciiValue!) + UInt8(v)))
                if n % 2 == 0 || pos != n - 1 - pos { digits[n - 1 - pos] = digits[pos] }
            }
            return String(digits)
        case 7:
            return largestPal7(n)
        default:
            return String(digits)
        }
    }

    private func largestPal7(_ n: Int) -> String {
        let halfLen = (n + 1) / 2
        var half = Array(repeating: Character("9"), count: halfLen)
        while true {
            var pal = Array(repeating: Character("0"), count: n)
            for i in 0..<halfLen { pal[i] = half[i] }
            for i in 0..<(n / 2) { pal[n - 1 - i] = pal[i] }
            if mod7(String(pal)) == 0 { return String(pal) }
            var idx = halfLen - 1
            while idx >= 0 && half[idx] == "0" {
                half[idx] = "9"
                idx -= 1
            }
            if idx < 0 { break }
            let v = Int(half[idx].asciiValue! - Character("0").asciiValue!) - 1
            half[idx] = Character(UnicodeScalar(UInt8(Character("0").asciiValue!) + UInt8(v)))
        }
        return ""
    }

    private func mod7(_ s: String) -> Int {
        var r = 0
        for c in s { r = (r * 10 + Int(c.asciiValue! - Character("0").asciiValue!)) % 7 }
        return r
    }
}
