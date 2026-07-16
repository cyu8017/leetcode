// LeetCode 0492 - Construct the Rectangle
// https://leetcode.com/problems/construct-the-rectangle/

class Solution {
    func constructRectangle(_ area: Int) -> [Int] {
        var width = Int(Double(area).squareRoot())
        while width > 0 {
            if area % width == 0 {
                return [area / width, width]
            }
            width -= 1
        }
        return [area, 1]
    }
}
