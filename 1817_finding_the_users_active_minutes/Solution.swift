// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

class Solution {
    func findingUsersActiveMinutes(_ logs: [[Int]], _ k: Int) -> [Int] {
        var userMinutes = [Int: Set<Int>]()
        for log in logs {
            userMinutes[log[0], default: []].insert(log[1])
        }
        var answer = Array(repeating: 0, count: k)
        for minutes in userMinutes.values {
            let uam = minutes.count
            if uam <= k {
                answer[uam - 1] += 1
            }
        }
        return answer
    }
}
