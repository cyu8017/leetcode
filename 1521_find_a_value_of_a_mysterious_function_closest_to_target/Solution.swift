// LeetCode 1521 - Find a Value of a Mysterious Function Closest to Target
// https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

class Solution {
    func closestToTarget(_ arr: [Int], _ target: Int) -> Int {
        var answer = Int.max
        var current = Set<Int>()
        for value in arr {
            var next = Set<Int>([value])
            for prev in current { next.insert(value & prev) }
            current = next
            for candidate in current {
                answer = min(answer, abs(candidate - target))
            }
        }
        return answer
    }
}
