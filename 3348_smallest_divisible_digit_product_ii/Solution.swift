// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

class Solution {
    func smallestNumber(_ num: String, _ t: Int) -> String {
        var tt = t
        for d in stride(from: 9, through: 2, by: -1) {
            while tt % d == 0 { tt /= d }
        }
        if tt > 1 { return "-1" }
        let numArr = Array(num)
        for extra in 0...60 {
            let L = numArr.count + extra
            var res = Array(repeating: Character("0"), count: L)
            if dfs(&res, 0, true, extra == 0, numArr, t) { return String(res) }
        }
        return "-1"
    }

    private func dfs(_ res: inout [Character], _ i: Int, _ tight: Bool, _ sameLen: Bool, _ num: [Character], _ t: Int) -> Bool {
        if i == res.count {
            var prod = 1
            for c in res {
                prod *= Int(c.asciiValue! - 48)
                if prod == 0 { break }
            }
            return prod % t == 0 && prod > 0
        }
        var start: UInt8 = i == 0 ? 49 : 48
        if tight && sameLen && i < num.count { start = num[i].asciiValue! }
        var c = start
        while c <= 57 {
            res[i] = Character(UnicodeScalar(c))
            let nt = tight && sameLen && i < num.count && c == num[i].asciiValue!
            if dfs(&res, i + 1, nt, sameLen, num, t) { return true }
            c += 1
        }
        return false
    }
}
