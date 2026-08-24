// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

class Solution {
    func splitIntoFibonacci(_ num: String) -> [Int] {
        let chars = Array(num)
        var path = [Int]()
        func dfs(_ start: Int) -> Bool {
            if start == chars.count { return path.count >= 3 }
            var val = 0
            for end in start..<chars.count {
                if chars[start] == "0" && end > start { break }
                val = val * 10 + Int(chars[end].asciiValue! - Character("0").asciiValue!)
                if val > Int32.max { break }
                if path.count >= 2 {
                    let total = path[path.count - 1] + path[path.count - 2]
                    if val < total { continue }
                    if val > total { break }
                }
                path.append(val)
                if dfs(end + 1) { return true }
                path.removeLast()
            }
            return false
        }
        _ = dfs(0)
        return path
    }
}
