// LeetCode 1013 - Partition Array Into Three Parts With Equal Sum
// https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/

class Solution {
    func canThreePartsEqualSum(_ arr: [Int]) -> Bool {
        let total = arr.reduce(0, +)
        if total % 3 != 0 { return false }
        let target = total / 3
        var parts = 0, cur = 0
        for x in arr {
            cur += x
            if cur == target {
                parts += 1
                cur = 0
            }
        }
        return parts >= 3
    }
}
