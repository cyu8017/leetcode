// LeetCode 3324 - Find the Sequence of Strings Appeared on the Screen
// https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/

class Solution {
    func stringSequence(_ target: String) -> [String] {
        var ans = [String]()
        var cur = [Character]()
        for ch in target {
            cur.append("a")
            ans.append(String(cur))
            while cur[cur.count - 1] != ch {
                let v = Int(cur[cur.count - 1].asciiValue!) + 1
                cur[cur.count - 1] = Character(UnicodeScalar(v)!)
                ans.append(String(cur))
            }
        }
        return ans
    }
}
