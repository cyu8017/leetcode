// LeetCode 3211 - Generate Binary Strings Without Adjacent Zeros
// https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

class Solution {
    private var n = 0
    private var t: [Character] = []
    private var ans: [String] = []

    func validStrings(_ n: Int) -> [String] {
        self.n = n
        ans = []
        t = []
        dfs(0)
        return ans
    }

    private func dfs(_ i: Int) {
        if i >= n {
            ans.append(String(t))
            return
        }
        for j in 0..<2 {
            if (j == 0 && (i == 0 || t[i - 1] == "1")) || j == 1 {
                t.append(j == 0 ? "0" : "1")
                dfs(i + 1)
                t.removeLast()
            }
        }
    }
}
