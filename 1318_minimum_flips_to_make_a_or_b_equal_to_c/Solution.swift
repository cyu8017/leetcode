// LeetCode 1318 - Minimum Flips to Make a OR b Equal to c
// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution {
    func minFlips(_ a: Int, _ b: Int, _ c: Int) -> Int {
        var a = a, b = b, c = c, flips = 0
        while a > 0 || b > 0 || c > 0 {
            let bitA = a & 1, bitB = b & 1, bitC = c & 1
            if bitC == 0 { flips += bitA + bitB }
            else if bitA | bitB == 0 { flips += 1 }
            a >>= 1; b >>= 1; c >>= 1
        }
        return flips
    }
}
