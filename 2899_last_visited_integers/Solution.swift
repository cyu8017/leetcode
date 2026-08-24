// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

class Solution {
    func lastVisitedIntegers(_ nums: [Int]) -> [Int] {
        var seen: [Int] = []
        var ans: [Int] = []
        var k = 0
        for v in nums {
            if v != -1 {
                seen.append(v)
                k = 0
            } else {
                k += 1
                if k > seen.count { ans.append(-1) }
                else { ans.append(seen[seen.count - k]) }
            }
        }
        return ans
    }
}
