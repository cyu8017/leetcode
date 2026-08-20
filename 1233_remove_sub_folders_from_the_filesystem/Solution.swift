// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution {
    func removeSubfolders(_ folder: [String]) -> [String] {
        let sorted = folder.sorted()
        var ans: [String] = []
        for f in sorted {
            if ans.isEmpty || !f.hasPrefix(ans.last! + "/") {
                ans.append(f)
            }
        }
        return ans
    }
}
