// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

class Solution {
    func maximizeSquareHoleArea(_ n: Int, _ m: Int, _ hBars: [Int], _ vBars: [Int]) -> Int {
        let side = min(maxGap(hBars), maxGap(vBars))
        return side * side
    }

    private func maxGap(_ bars0: [Int]) -> Int {
        if bars0.isEmpty { return 1 }
        let bars = bars0.sorted()
        var best = 1, cur = 1
        for i in 1..<bars.count {
            if bars[i] == bars[i - 1] + 1 { cur += 1 }
            else { cur = 1 }
            best = max(best, cur)
        }
        return best + 1
    }
}
