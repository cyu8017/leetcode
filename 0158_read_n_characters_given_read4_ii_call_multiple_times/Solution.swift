// LeetCode 0158 - Read N Characters Given read4 II - Call Multiple Times
// https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

class Solution {
    func read(_ file: String, _ queries: [Int]) -> [Int] {
        let characters = Array(file)
        var fileIndex = 0
        var buffer = Array(repeating: Character(" "), count: 4)
        var bufferSize = 0
        var bufferIndex = 0
        var result: [Int] = []

        func read4() -> Int {
            var count = 0
            while count < 4 && fileIndex < characters.count {
                buffer[count] = characters[fileIndex]
                fileIndex += 1
                count += 1
            }
            return count
        }

        for query in queries {
            var copied = 0
            while copied < query {
                if bufferIndex == bufferSize {
                    bufferSize = read4()
                    bufferIndex = 0
                    if bufferSize == 0 {
                        break
                    }
                }
                let amount = min(query - copied, bufferSize - bufferIndex)
                copied += amount
                bufferIndex += amount
            }
            result.append(copied)
        }
        return result
    }
}