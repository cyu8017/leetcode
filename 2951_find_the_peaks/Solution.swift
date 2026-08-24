// LeetCode 2951 - Find the Peaks
// https://leetcode.com/problems/find-the-peaks/

class Solution {
    func findPeaks(_ mountain: [Int]) -> [Int] {
        var ans: [Int] = []
        for i in 1..<(mountain.count - 1) where mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1] {
            ans.append(i)
        }
        return ans
    }
}
