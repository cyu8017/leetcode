// LeetCode 0781 - Rabbits in Forest
// https://leetcode.com/problems/rabbits-in-forest/

class Solution {
    func numRabbits(_ answers: [Int]) -> Int {
        var counts = [Int: Int]()
        for answer in answers { counts[answer, default: 0] += 1 }
        var total = 0
        for (x, c) in counts {
            let group = x + 1
            let groups = (c + group - 1) / group
            total += groups * group
        }
        return total
    }
}
