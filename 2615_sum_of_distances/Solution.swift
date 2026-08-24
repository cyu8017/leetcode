// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

class Solution {
    func distance(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = [Int](repeating: 0, count: n)
        var pos = [Int: [Int]]()
        for i in 0..<n { pos[nums[i], default: []].append(i) }
        for idxs in pos.values {
            let m = idxs.count
            var pref = [Int](repeating: 0, count: m + 1)
            for i in 0..<m { pref[i + 1] = pref[i] + idxs[i] }
            for j in 0..<m {
                let idx = idxs[j]
                let left = j * idx - pref[j]
                let right = pref[m] - pref[j + 1] - (m - 1 - j) * idx
                ans[idx] = left + right
            }
        }
        return ans
    }
}
