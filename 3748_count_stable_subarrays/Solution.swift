// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/

class Solution {
    func countStableSubarrays(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var seg = [Int]()
        var s = [0]
        var l = 0
        for r in 0..<n {
            if r == n - 1 || nums[r] > nums[r + 1] {
                seg.append(l)
                let k = r - l + 1
                s.append(s[s.count - 1] + k * (k + 1) / 2)
                l = r + 1
            }
        }
        var ans = [Int](repeating: 0, count: queries.count)
        for idx in 0..<queries.count {
            let left = queries[idx][0], right = queries[idx][1]
            let i = lowerBound(seg, left + 1)
            let j = lowerBound(seg, right + 1) - 1
            if i > j {
                let k = right - left + 1
                ans[idx] = k * (k + 1) / 2
            } else {
                let a = seg[i] - left
                let b = right - seg[j] + 1
                ans[idx] = a * (a + 1) / 2 + s[j] - s[i] + b * (b + 1) / 2
            }
        }
        return ans
    }

    private func lowerBound(_ a: [Int], _ x: Int) -> Int {
        var lo = 0, hi = a.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if a[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo
    }
}
