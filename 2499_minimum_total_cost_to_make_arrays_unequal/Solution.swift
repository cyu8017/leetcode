// LeetCode 2499 - Minimum Total Cost to Make Arrays Unequal
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

class Solution {
    func minimumTotalCost(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let n = nums1.count
        var freq = [Int: Int]()
        var ans = 0, same = 0
        for i in 0..<n where nums1[i] == nums2[i] {
            same += 1
            freq[nums1[i], default: 0] += 1
            ans += i
        }
        var maxFreq = 0, maxVal = 0
        for (k, v) in freq {
            if v > maxFreq {
                maxFreq = v
                maxVal = k
            }
        }
        var need = maxFreq * 2 - same
        if need <= 0 { return ans }
        for i in 0..<n where need > 0 {
            if nums1[i] != nums2[i] && nums1[i] != maxVal && nums2[i] != maxVal {
                ans += i
                need -= 1
            }
        }
        return need > 0 ? -1 : ans
    }
}
