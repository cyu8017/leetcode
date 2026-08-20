// LeetCode 1465 - Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

class Solution {
    func maxArea(_ h: Int, _ w: Int, _ horizontalCuts: [Int], _ verticalCuts: [Int]) -> Int {
        let hs = ([0, h] + horizontalCuts).sorted()
        let vs = ([0, w] + verticalCuts).sorted()
        var maxH = 0, maxV = 0
        for i in 1..<hs.count { maxH = max(maxH, hs[i] - hs[i - 1]) }
        for i in 1..<vs.count { maxV = max(maxV, vs[i] - vs[i - 1]) }
        return (maxH * maxV) % 1_000_000_007
    }
}
