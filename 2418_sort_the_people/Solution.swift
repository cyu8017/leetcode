// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

class Solution {
    func sortPeople(_ names: [String], _ heights: [Int]) -> [String] {
        let n = names.count
        var idx = Array(0..<n)
        idx.sort { heights[$0] > heights[$1] }
        return idx.map { names[$0] }
    }
}
