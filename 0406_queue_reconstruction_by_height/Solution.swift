// LeetCode 0406 - Queue Reconstruction by Height
// https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution {
    func reconstructQueue(_ people: [[Int]]) -> [[Int]] {
        let sorted = people.sorted {
            if $0[0] == $1[0] {
                return $0[1] < $1[1]
            }
            return $0[0] > $1[0]
        }

        var queue: [[Int]] = []
        for person in sorted {
            queue.insert(person, at: person[1])
        }
        return queue
    }
}
