// LeetCode 0277 - Find the Celebrity
// https://leetcode.com/problems/find-the-celebrity/

func knows(_ a: Int, _ b: Int) -> Bool {
    false
}

class Solution {
    func findCelebrity(_ n: Int) -> Int {
        var candidate = 0
        for person in 1..<n {
            if knows(candidate, person) {
                candidate = person
            }
        }
        for person in 0..<n {
            if person == candidate {
                continue
            }
            if knows(candidate, person) || !knows(person, candidate) {
                return -1
            }
        }
        return candidate
    }
}
