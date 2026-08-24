// LeetCode 3720 - Lexicographically Smallest Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

class Solution {
    private var cnt = [Int]()
    private var ans = [Character]()
    private var targetChars = [Character]()
    private var n = 0

    func lexGreaterPermutation(_ s: String, _ target: String) -> String {
        cnt = [Int](repeating: 0, count: 26)
        for c in s { cnt[Int(c.asciiValue! - 97)] += 1 }
        n = s.count
        targetChars = Array(target)
        ans = [Character](repeating: "a", count: n)
        if dfs(0, false) { return String(ans) }
        return ""
    }

    private func dfs(_ pos: Int, _ greater: Bool) -> Bool {
        if pos == n { return greater }
        let start = greater ? 0 : Int(targetChars[pos].asciiValue! - 97)
        if start < 0 { return false }
        for c in start..<26 {
            if cnt[c] == 0 { continue }
            cnt[c] -= 1
            ans[pos] = Character(UnicodeScalar(97 + c)!)
            let ng = greater || c > Int(targetChars[pos].asciiValue! - 97)
            if dfs(pos + 1, ng) { return true }
            cnt[c] += 1
        }
        return false
    }
}
