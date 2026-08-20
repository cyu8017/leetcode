// LeetCode 1436 - Destination City
// https://leetcode.com/problems/destination-city/

class Solution {
    func destCity(_ paths: [[String]]) -> String {
        let starts = Set(paths.map { $0[0] })
        return paths.first { !starts.contains($0[1]) }![1]
    }
}
