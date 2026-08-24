// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

class Solution {
    func goodIndices(_ nums: [Int], _ k: Int) -> [Int] {
        let n = nums.count
        var dec = [Int](repeating: 0, count: n)
        var inc = [Int](repeating: 0, count: n)
        dec[0] = 1
        for i in 1..<n {
            dec[i] = nums[i] <= nums[i - 1] ? dec[i - 1] + 1 : 1
        }
        inc[n - 1] = 1
        for i in stride(from: n - 2, through: 0, by: -1) {
            inc[i] = nums[i] <= nums[i + 1] ? inc[i + 1] + 1 : 1
        }
        var ans = [Int]()
        if n > 2 * k {
            for i in k..<(n - k) {
                if dec[i - 1] >= k && inc[i + 1] >= k { ans.append(i) }
            }
        }
        return ans
    }
}
