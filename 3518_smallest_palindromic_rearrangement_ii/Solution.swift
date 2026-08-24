// LeetCode 3518 - Smallest Palindromic Rearrangement II
// https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/

class Solution {
    let MAX = 1000001

    func nCk(_ n: Int, _ kk0: Int) -> Int {
        var kk = kk0
        if kk < 0 || kk > n { return 0 }
        var res = 1
        if kk > n - kk { kk = n - kk }
        if kk > 0 {
            for i in 1...kk {
                res = res * (n - i + 1) / i
                if res >= MAX { return MAX }
            }
        }
        return res
    }

    func countArr(_ h: [Int]) -> Int {
        var total = 0
        for f in h { total += f }
        var res = 1
        for f in h {
            res *= nCk(total, f)
            if res >= MAX { return MAX }
            total -= f
        }
        return res
    }

    func smallestPalindrome(_ s: String, _ k0: Int) -> String {
        var k = k0
        var cnt = Array(repeating: 0, count: 26)
        for c in s.utf8 { cnt[Int(c - 97)] += 1 }
        var odd = 0
        for c in cnt where c % 2 != 0 { odd += 1 }
        if odd > 1 { return "" }
        var half = Array(repeating: 0, count: 26)
        var mid: Character? = nil
        for i in 0..<26 {
            half[i] = cnt[i] / 2
            if cnt[i] % 2 != 0 { mid = Character(UnicodeScalar(97 + i)!) }
        }
        if countArr(half) < k { return "" }
        var halfLen = 0
        for f in half { halfLen += f }
        var left: [Character] = []
        if halfLen > 0 {
            for _ in 0..<halfLen {
                for i in 0..<26 {
                    if half[i] == 0 { continue }
                    half[i] -= 1
                    let arr = countArr(half)
                    if arr >= k {
                        left.append(Character(UnicodeScalar(97 + i)!))
                        break
                    }
                    k -= arr
                    half[i] += 1
                }
            }
        }
        var res = left
        if let mid = mid { res.append(mid) }
        for i in stride(from: left.count - 1, through: 0, by: -1) { res.append(left[i]) }
        return String(res)
    }
}
