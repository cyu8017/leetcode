// LeetCode 0157 - Read N Characters Given Read4
// https://leetcode.com/problems/read-n-characters-given-read4/

class Solution {
    func read(_ file: String, _ n: Int) -> Int {
        let characters = Array(file)
        var fileIndex = 0
        var copied = 0

        func read4(_ buffer: inout [Character]) -> Int {
            var count = 0
            while count < 4 && fileIndex < characters.count {
                buffer[count] = characters[fileIndex]
                fileIndex += 1
                count += 1
            }
            return count
        }

        while copied < n {
            var buffer = Array(repeating: Character(" "), count: 4)
            let count = read4(&buffer)
            if count == 0 {
                break
            }
            copied += min(count, n - copied)
        }
        return copied
    }
}