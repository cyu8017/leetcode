// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

class Solution {
    func pathInZigZagTree(_ label: Int) -> [Int] {
        var label = label
        var path = [label]
        while label > 1 {
            let level = Int.bitWidth - label.leadingZeroBitCount - 1
            label >>= 1
            label = (1 << level) - 1 - label + (1 << (level - 1))
            path.append(label)
        }
        return path.reversed()
    }
}
