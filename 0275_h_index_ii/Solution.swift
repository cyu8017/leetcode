// LeetCode 0275 - H-Index II
// https://leetcode.com/problems/h-index-ii/

class Solution {
    func hIndex(_ citations: [Int]) -> Int {
        var left = 0
        var right = citations.count - 1
        let length = citations.count
        while left <= right {
            let mid = (left + right) / 2
            let papers = length - mid
            if citations[mid] >= papers {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
        return length - left
    }
}
