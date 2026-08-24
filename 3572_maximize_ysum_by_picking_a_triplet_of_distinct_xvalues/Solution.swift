// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

class Solution {
    func maxSumDistinctTriplet(_ x: [Int], _ y: [Int]) -> Int {
        let n = x.count
        var arr = (0..<n).map { [x[$0], y[$0]] }
        arr.sort { $0[1] > $1[1] }
        var ans = 0
        var vis = Set<Int>()
        for i in 0..<n {
            let a = arr[i][0], b = arr[i][1]
            if !vis.contains(a) {
                vis.insert(a)
                ans += b
                if vis.count == 3 { return ans }
            }
        }
        return -1
    }
}
