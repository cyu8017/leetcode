// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

class Solution {
    func canMakePalindromeQueries(_ s: String, _ queries: [[Int]]) -> [Bool] {
        let n = s.count
        let m = n / 2
        let all = Array(s)
        var tArr = Array(all[m..<n])
        tArr.reverse()
        let sArr = Array(all[0..<m])
        var pre1 = Array(repeating: Array(repeating: 0, count: 26), count: m + 1)
        var pre2 = Array(repeating: Array(repeating: 0, count: 26), count: m + 1)
        var diff = Array(repeating: 0, count: m + 1)
        let aVal = Int(Character("a").asciiValue!)
        for i in 1...m {
            pre1[i] = pre1[i - 1]
            pre2[i] = pre2[i - 1]
            pre1[i][Int(sArr[i - 1].asciiValue!) - aVal] += 1
            pre2[i][Int(tArr[i - 1].asciiValue!) - aVal] += 1
            diff[i] = diff[i - 1] + (sArr[i - 1] == tArr[i - 1] ? 0 : 1)
        }
        var ans: [Bool] = []
        for q in queries {
            let a = q[0], b = q[1]
            let c = n - 1 - q[3], d = n - 1 - q[2]
            if a <= c {
                ans.append(check(pre1, pre2, diff, a, b, c, d))
            } else {
                ans.append(check(pre2, pre1, diff, c, d, a, b))
            }
        }
        return ans
    }

    private func check(_ pre1: [[Int]], _ pre2: [[Int]], _ diff: [Int], _ a: Int, _ b: Int, _ c: Int, _ d: Int) -> Bool {
        if diff[a] > 0 || diff[diff.count - 1] - diff[max(b, d) + 1] > 0 { return false }
        if d <= b { return eq(count(pre1, a, b), count(pre2, a, b)) }
        if b < c {
            return diff[c] - diff[b + 1] == 0
                && eq(count(pre1, a, b), count(pre2, a, b))
                && eq(count(pre1, c, d), count(pre2, c, d))
        }
        guard let cnt1 = sub(count(pre1, a, b), count(pre2, a, c - 1)),
              let cnt2 = sub(count(pre2, c, d), count(pre1, b + 1, d)) else { return false }
        return eq(cnt1, cnt2)
    }

    private func count(_ pre: [[Int]], _ i: Int, _ j: Int) -> [Int] {
        var cnt = Array(repeating: 0, count: 26)
        for k in 0..<26 { cnt[k] = pre[j + 1][k] - pre[i][k] }
        return cnt
    }

    private func sub(_ cnt1: [Int], _ cnt2: [Int]) -> [Int]? {
        var cnt = Array(repeating: 0, count: 26)
        for i in 0..<26 {
            cnt[i] = cnt1[i] - cnt2[i]
            if cnt[i] < 0 { return nil }
        }
        return cnt
    }

    private func eq(_ a: [Int], _ b: [Int]) -> Bool {
        return a == b
    }
}
