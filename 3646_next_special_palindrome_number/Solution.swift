// LeetCode 3646 - Next Special Palindrome Number
// https://leetcode.com/problems/next-special-palindrome-number/

class Solution {
    var cands = [Int]()
    var halfCnt = [Int]()
    var mid = 0
    var halfLen = 0

    func dfs(_ pos: Int, _ cur: inout [Int]) {
        if pos == halfLen {
            var left = ""
            for x in cur { left += String(x) }
            var s = left
            if mid > 0 { s += String(mid) }
            s += String(left.reversed())
            cands.append(Int(s)!)
            return
        }
        for d in 1...9 {
            if halfCnt[d] == 0 { continue }
            halfCnt[d] -= 1
            cur.append(d)
            dfs(pos + 1, &cur)
            cur.removeLast()
            halfCnt[d] += 1
        }
    }

    func gen(_ mask: Int) {
        var total = 0, odd = 0
        for d in 1...9 {
            if ((mask >> d) & 1) != 0 {
                total += d
                if d % 2 == 1 { odd += 1 }
            }
        }
        if total == 0 || total > 18 || odd > 1 { return }
        halfCnt = Array(repeating: 0, count: 10)
        mid = 0
        for d in 1...9 {
            if ((mask >> d) & 1) == 0 { continue }
            halfCnt[d] = d / 2
            if d % 2 == 1 { mid = d }
        }
        halfLen = total / 2
        var cur = [Int]()
        dfs(0, &cur)
    }

    func specialPalindrome(_ n: Int) -> Int {
        cands = []
        for mask in 1..<(1 << 10) {
            if (mask & 1) != 0 { continue }
            gen(mask)
        }
        cands.sort()
        for v in cands where v > n { return v }
        return -1
    }
}
