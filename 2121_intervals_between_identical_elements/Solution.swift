// LeetCode 2121 - Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/

class Solution {
    func getDistances(_ arr: [Int]) -> [Int] {
        var pos = [Int: [Int]]()
        for i in 0..<arr.count { pos[arr[i], default: []].append(i) }
        var ans = [Int](repeating: 0, count: arr.count)
        for idxs in pos.values {
            let m = idxs.count
            var pref = [Int](repeating: 0, count: m + 1)
            for i in 0..<m { pref[i + 1] = pref[i] + idxs[i] }
            for i in 0..<m {
                let left = i * idxs[i] - pref[i]
                let right = (pref[m] - pref[i + 1]) - (m - i - 1) * idxs[i]
                ans[idxs[i]] = left + right
            }
        }
        return ans
    }
}
