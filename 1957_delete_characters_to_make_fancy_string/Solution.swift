// LeetCode 1957 - Delete Characters to Make Fancy String
// https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution {
    func makeFancyString(_ s: String) -> String {
        var ans: [Character] = []
        for c in s {
            if ans.count >= 2 && ans[ans.count - 1] == c && ans[ans.count - 2] == c {
                continue
            }
            ans.append(c)
        }
        return String(ans)
    }
}
