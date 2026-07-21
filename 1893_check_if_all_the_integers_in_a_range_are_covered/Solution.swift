// LeetCode 1893 - Check if All the Integers in a Range Are Covered
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

class Solution {
    func isCovered(_ ranges: [[Int]], _ left: Int, _ right: Int) -> Bool {
        var covered = [Bool](repeating: false, count: 51)
        for range in ranges {
            let start = range[0]
            let end = range[1]
            for value in start...end {
                covered[value] = true
            }
        }
        for value in left...right {
            if !covered[value] {
                return false
            }
        }
        return true
    }
}
