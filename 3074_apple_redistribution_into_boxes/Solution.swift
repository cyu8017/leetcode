// LeetCode 3074 - Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/

class Solution {
    func minimumBoxes(_ apple: [Int], _ capacity: [Int]) -> Int {
        let cap = capacity.sorted()
        var s = apple.reduce(0, +)
        var i = 1
        while true {
            s -= cap[cap.count - i]
            if s <= 0 { return i }
            i += 1
        }
    }
}
