// LeetCode 1726 - Tuple with Same Product
// https://leetcode.com/problems/tuple-with-same-product/

class Solution {
    func tupleSameProduct(_ nums: [Int]) -> Int {
        var counts = [Int: Int]()
        for i in 0..<nums.count {
            for j in (i + 1)..<nums.count {
                counts[nums[i] * nums[j], default: 0] += 1
            }
        }
        var result = 0
        for count in counts.values {
            result += count * (count - 1) * 4
        }
        return result
    }
}
