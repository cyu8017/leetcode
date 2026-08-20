// LeetCode 1593 - Split a String Into the Max Number of Unique Substrings
// https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/

class Solution {
    func maxUniqueSplit(_ s: String) -> Int {
        let chars = Array(s)
        var used = Set<String>()
        var answer = 0
        func dfs(_ i: Int) {
            if used.count + chars.count - i <= answer { return }
            if i == chars.count {
                answer = max(answer, used.count)
                return
            }
            for j in (i + 1)...chars.count {
                let part = String(chars[i..<j])
                if !used.contains(part) {
                    used.insert(part)
                    dfs(j)
                    used.remove(part)
                }
            }
        }
        dfs(0)
        return answer
    }
}
