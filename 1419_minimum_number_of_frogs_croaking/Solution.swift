// LeetCode 1419 - Minimum Number of Frogs Croaking
// https://leetcode.com/problems/minimum-number-of-frogs-croaking/

class Solution {
    func minNumberOfFrogs(_ croakOfFrogs: String) -> Int {
        let order: [Character: Int] = ["c":0,"r":1,"o":2,"a":3,"k":4]
        var counts = Array(repeating: 0, count: 5)
        var active = 0, answer = 0
        for char in croakOfFrogs {
            guard let i = order[char] else { return -1 }
            if i > 0 && counts[i - 1] == 0 { return -1 }
            if i > 0 { counts[i - 1] -= 1 }
            counts[i] += 1
            if i == 0 {
                active += 1
                answer = max(answer, active)
            } else if i == 4 {
                counts[4] -= 1
                active -= 1
            }
        }
        return active == 0 ? answer : -1
    }
}
