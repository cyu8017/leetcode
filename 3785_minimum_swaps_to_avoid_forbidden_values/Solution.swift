// LeetCode 3785 - Minimum Swaps to Avoid Forbidden Values
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/

class Solution {
    func minSwaps(_ nums: [Int], _ forbidden: [Int]) -> Int {
        let n = nums.count
        var freq = [Int: Int]()
        for x in nums { freq[x, default: 0] += 1 }
        for x in forbidden { freq[x, default: 0] += 1 }
        for c in freq.values {
            if c > n { return -1 }
        }
        var bad = [Int: Int]()
        var total = 0, largest = 0
        for i in 0..<n {
            if nums[i] == forbidden[i] {
                bad[nums[i], default: 0] += 1
                total += 1
                if bad[nums[i]]! > largest { largest = bad[nums[i]]! }
            }
        }
        if (total + 1) / 2 > largest { return (total + 1) / 2 }
        return largest
    }
}
