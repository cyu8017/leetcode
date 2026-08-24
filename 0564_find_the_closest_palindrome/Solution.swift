// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/

class Solution {
    func nearestPalindromic(_ n: String) -> String {
        let length = n.count
        let number = Int(n)!
        var candidates = [pow10(length - 1) - 1, pow10(length) + 1]
        let prefix = Int(String(n.prefix((length + 1) / 2)))!
        for half in (prefix - 1)...(prefix + 1) {
            candidates.append(makePalindrome(half, length))
        }
        var best = -1
        var bestDiff = Int.max
        for candidate in candidates {
            if candidate == number { continue }
            let diff = abs(candidate - number)
            if diff < bestDiff || (diff == bestDiff && candidate < best) {
                best = candidate
                bestDiff = diff
            }
        }
        return String(best)
    }

    private func makePalindrome(_ half: Int, _ length: Int) -> Int {
        let text = Array(String(half))
        var pal = text
        if length % 2 == 0 {
            pal += text.reversed()
        } else if text.count >= 2 {
            pal += text.dropLast().reversed()
        }
        return Int(String(pal))!
    }

    private func pow10(_ exp: Int) -> Int {
        var value = 1
        for _ in 0..<exp { value *= 10 }
        return value
    }
}
