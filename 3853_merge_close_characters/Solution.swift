// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

class Solution {
    func mergeCharacters(_ s: String, _ k: Int) -> String {
        var last = [Character: Int]()
        var ans = [Character]()
        for c in s {
            let cur = ans.count
            if let p = last[c], cur - p <= k { continue }
            ans.append(c)
            last[c] = cur
        }
        return String(ans)
    }
}
