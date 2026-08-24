// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution {
    func findDuplicate(_ paths: [String]) -> [[String]] {
        var contentToPaths = [String: [String]]()
        for entry in paths {
            let tokens = entry.split(separator: " ").map(String.init)
            let directory = tokens[0]
            for i in 1..<tokens.count {
                let fileInfo = tokens[i]
                let open = fileInfo.firstIndex(of: "(")!
                let name = String(fileInfo[..<open])
                let content = String(fileInfo[fileInfo.index(after: open)..<fileInfo.index(before: fileInfo.endIndex)])
                contentToPaths[content, default: []].append(directory + "/" + name)
            }
        }
        return contentToPaths.values.filter { $0.count > 1 }
    }
}
