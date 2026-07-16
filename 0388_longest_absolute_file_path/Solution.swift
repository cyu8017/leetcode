// LeetCode 0388 - Longest Absolute File Path
// https://leetcode.com/problems/longest-absolute-file-path/

class Solution {
    func lengthLongestPath(_ input: String) -> Int {
        var stack: [Int] = []
        var maxLength = 0

        for line in input.split(separator: "\n", omittingEmptySubsequences: false) {
            let lineText = String(line)
            var depth = 0
            while depth < lineText.count && lineText[lineText.index(lineText.startIndex, offsetBy: depth)] == "\t" {
                depth += 1
            }
            let name = String(lineText.dropFirst(depth))

            while stack.count > depth {
                stack.removeLast()
            }

            if name.contains(".") {
                let prefix = stack.last ?? 0
                maxLength = max(maxLength, name.count + prefix)
            } else {
                let prefix = stack.last ?? 0
                stack.append(prefix + name.count + 1)
            }
        }

        return maxLength
    }
}
