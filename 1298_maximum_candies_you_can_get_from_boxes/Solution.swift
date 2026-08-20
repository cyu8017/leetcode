// LeetCode 1298 - Maximum Candies You Can Get from Boxes
// https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

class Solution {
    func maxCandies(_ status: [Int], _ candies: [Int], _ keys: [[Int]], _ containedBoxes: [[Int]], _ initialBoxes: [Int]) -> Int {
        var haveBox = Set(initialBoxes)
        var haveKey = Set<Int>()
        var opened = Set<Int>()
        var ans = 0
        var changed = true
        while changed {
            changed = false
            for box in Array(haveBox) where !opened.contains(box) {
                if status[box] == 1 || haveKey.contains(box) {
                    opened.insert(box)
                    ans += candies[box]
                    for k in keys[box] { haveKey.insert(k) }
                    for b in containedBoxes[box] { haveBox.insert(b) }
                    changed = true
                }
            }
        }
        return ans
    }
}
