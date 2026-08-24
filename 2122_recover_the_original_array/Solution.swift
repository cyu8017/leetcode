// LeetCode 2122 - Recover the Original Array
// https://leetcode.com/problems/recover-the-original-array/

class Solution {
    func recoverArray(_ nums: [Int]) -> [Int] {
        let nums = nums.sorted()
        let n = nums.count
        for i in 1..<n {
            let diff = nums[i] - nums[0]
            if diff == 0 || diff % 2 != 0 { continue }
            let k = diff / 2
            var used = [Bool](repeating: false, count: n)
            used[0] = true; used[i] = true
            var ans = [(nums[0] + nums[i]) / 2]
            var l = 0, r = i, ok = true
            while ans.count < n / 2 {
                while l < n && used[l] { l += 1 }
                if l == n { ok = false; break }
                let need = nums[l] + 2 * k
                while r < n && (used[r] || nums[r] < need) { r += 1 }
                if r == n || nums[r] != need { ok = false; break }
                used[l] = true; used[r] = true
                ans.append(nums[l] + k)
            }
            if ok { return ans }
        }
        return []
    }
}
