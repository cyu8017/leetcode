// LeetCode 1487 - Making File Names Unique
// https://leetcode.com/problems/making-file-names-unique/

class Solution {
    func getFolderNames(_ names: [String]) -> [String] {
        var used = [String: Int](), ans = [String]()
        for name in names {
            let candidate: String
            if used[name] == nil {
                candidate = name
            } else {
                var k = used[name]!
                while used["\(name)(\(k))"] != nil { k += 1 }
                candidate = "\(name)(\(k))"
                used[name] = k + 1
            }
            used[candidate] = 1
            ans.append(candidate)
        }
        return ans
    }
}
