// LeetCode 0986 - Interval List Intersections
// https://leetcode.com/problems/interval-list-intersections/

class Solution {
    func intervalIntersection(_ firstList: [[Int]], _ secondList: [[Int]]) -> [[Int]] {
        var i = 0, j = 0
        var ans = [[Int]]()
        while i < firstList.count && j < secondList.count {
            let lo = max(firstList[i][0], secondList[j][0])
            let hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi { ans.append([lo, hi]) }
            if firstList[i][1] < secondList[j][1] { i += 1 }
            else { j += 1 }
        }
        return ans
    }
}
