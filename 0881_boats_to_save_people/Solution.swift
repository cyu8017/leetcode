// LeetCode 0881 - Boats to Save People
// https://leetcode.com/problems/boats-to-save-people/

class Solution {
    func numRescueBoats(_ people: [Int], _ limit: Int) -> Int {
        let p = people.sorted()
        var i = 0, j = p.count - 1, boats = 0
        while i <= j {
            if p[i] + p[j] <= limit { i += 1 }
            j -= 1
            boats += 1
        }
        return boats
    }
}
