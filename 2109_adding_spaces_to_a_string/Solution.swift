// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution {
    func addSpaces(_ s: String, _ spaces: [Int]) -> String {
        let chars = Array(s)
        var b = [Character]()
        var j = 0
        for i in 0..<chars.count {
            if j < spaces.count && spaces[j] == i { b.append(" "); j += 1 }
            b.append(chars[i])
        }
        return String(b)
    }
}
