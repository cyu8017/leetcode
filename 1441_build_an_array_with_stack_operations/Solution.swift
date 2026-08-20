// LeetCode 1441 - Build an Array With Stack Operations
// https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution {
    func buildArray(_ target: [Int], _ n: Int) -> [String] {
        var answer = [String](), current = 1
        for value in target {
            while current < value {
                answer.append("Push"); answer.append("Pop"); current += 1
            }
            answer.append("Push"); current += 1
        }
        return answer
    }
}
