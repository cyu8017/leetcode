// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

class Solution {
    var words = [String]()
    var n = 0
    var tm = [Int: Int]()

    func calc(_ s: String, _ t: String) -> Int {
        let a = Array(s), b = Array(t)
        let m = min(a.count, b.count)
        for k in 0..<m where a[k] != b[k] { return k }
        return m
    }

    func add(_ i: Int, _ j: Int) {
        if i >= 0 && i < n && j >= 0 && j < n {
            tm[calc(words[i], words[j]), default: 0] += 1
        }
    }

    func remove(_ i: Int, _ j: Int) {
        if i >= 0 && i < n && j >= 0 && j < n {
            let x = calc(words[i], words[j])
            let c = tm[x]!
            if c == 1 { tm[x] = nil } else { tm[x] = c - 1 }
        }
    }

    func longestCommonPrefix(_ words: [String]) -> [Int] {
        self.words = words
        n = words.count
        tm = [:]
        if n > 1 {
            for i in 0..<(n - 1) { add(i, i + 1) }
        }
        var ans = Array(repeating: 0, count: n)
        for i in 0..<n {
            remove(i, i + 1)
            remove(i - 1, i)
            add(i - 1, i + 1)
            if let mx = tm.keys.max(), mx > 0 { ans[i] = mx }
            remove(i - 1, i + 1)
            add(i - 1, i)
            add(i, i + 1)
        }
        return ans
    }
}
