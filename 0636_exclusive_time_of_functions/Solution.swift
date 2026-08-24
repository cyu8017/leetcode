// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/

class Solution {
    func exclusiveTime(_ n: Int, _ logs: [String]) -> [Int] {
        var result = Array(repeating: 0, count: n)
        var stack = [Int]()
        var prevTime = 0
        for log in logs {
            let parts = log.split(separator: ":").map(String.init)
            let funcId = Int(parts[0])!
            let event = parts[1]
            let time = Int(parts[2])!
            if event == "start" {
                if let last = stack.last {
                    result[last] += time - prevTime
                }
                stack.append(funcId)
                prevTime = time
            } else {
                result[stack.removeLast()] += time - prevTime + 1
                prevTime = time + 1
            }
        }
        return result
    }
}
