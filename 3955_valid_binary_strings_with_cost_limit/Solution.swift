// LeetCode 3955 - Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/


class Solution {
    func generateValidStrings(_ n: Int, _ k: Int) -> [String] {
        var ans = [String]()
        var path = [Character]()
        func dfs(_ i: Int, _ tot: Int) {
            if i >= n {
                ans.append(String(path))
                return
            }
            path.append("0")
            dfs(i + 1, tot)
            path.removeLast()
            if (path.isEmpty || path.last == "0") && tot + i <= k {
                path.append("1")
                dfs(i + 1, tot + i)
                path.removeLast()
            }
        }
        dfs(0, 0)
        return ans
    }
}
