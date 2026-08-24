// LeetCode 3728 - Stable Subarrays With Equal Boundary And Interior Sum
// https://leetcode.com/problems/stable-subarrays-with-equal-boundary-and-interior-sum/

class Solution {
    func countStableSubarrays(_ capacity: [Int]) -> Int {
        let n = capacity.count
        var s = [Int](repeating: 0, count: n + 1)
        for i in 1...n { s[i] = s[i - 1] + capacity[i - 1] }
        var cnt = [String: Int]()
        var ans = 0
        if n > 2 {
            for r in 2..<n {
                let l = r - 2
                let keyL = "\(capacity[l])#\(capacity[l] + s[l + 1])"
                cnt[keyL, default: 0] += 1
                let keyR = "\(capacity[r])#\(s[r])"
                ans += cnt[keyR, default: 0]
            }
        }
        return ans
    }
}
