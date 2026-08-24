// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution {
    func getSneakyNumbers(_ nums: [Int]) -> [Int] {
        var seen = Set<Int>()
        var ans = [Int]()
        for x in nums {
            if !seen.insert(x).inserted { ans.append(x) }
        }
        return ans
    }
}
