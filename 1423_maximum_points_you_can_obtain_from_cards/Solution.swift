// LeetCode 1423 - Maximum Points You Can Obtain from Cards
// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution {
    func maxScore(_ cardPoints: [Int], _ k: Int) -> Int {
        if k == cardPoints.count { return cardPoints.reduce(0, +) }
        let window = cardPoints.count - k
        var current = cardPoints.prefix(window).reduce(0, +)
        var smallest = current
        for i in window..<cardPoints.count {
            current += cardPoints[i] - cardPoints[i - window]
            smallest = min(smallest, current)
        }
        return cardPoints.reduce(0, +) - smallest
    }
}
