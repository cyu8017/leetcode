// LeetCode 0466 - Count The Repetitions
// https://leetcode.com/problems/count-the-repetitions/

class Solution {
    func getMaxRepetitions(_ s1: String, _ n1: Int, _ s2: String, _ n2: Int) -> Int {
        if s2.isEmpty {
            return 0
        }

        let chars1 = Array(s1)
        let chars2 = Array(s2)
        var index = 0
        var s2Count = 0
        var record: [Int: (Int, Int)] = [:]

        for repeatIndex in 0..<n1 {
            for char in chars1 {
                if char == chars2[index] {
                    index += 1
                    if index == chars2.count {
                        index = 0
                        s2Count += 1
                    }
                }
            }

            if let previous = record[index] {
                let cycle = repeatIndex - previous.0
                let countCycle = s2Count - previous.1
                let remaining = n1 - repeatIndex - 1
                s2Count += (remaining / cycle) * countCycle
                if repeatIndex + (remaining / cycle) * cycle >= n1 - 1 {
                    break
                }
            }
            record[index] = (repeatIndex, s2Count)
        }

        return s2Count / n2
    }
}
