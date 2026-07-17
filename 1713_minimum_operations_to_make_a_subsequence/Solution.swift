// LeetCode 1713 - Minimum Operations to Make a Subsequence
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

class Solution {
    func minOperations(_ target: [Int], _ arr: [Int]) -> Int {
        var pos = [Int: Int]()
        for (i, value) in target.enumerated() {
            pos[value] = i
        }
        var lis = [Int]()
        for value in arr {
            guard let idx = pos[value] else {
                continue
            }
            var lo = 0
            var hi = lis.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if lis[mid] < idx {
                    lo = mid + 1
                } else {
                    hi = mid
                }
            }
            if lo == lis.count {
                lis.append(idx)
            } else {
                lis[lo] = idx
            }
        }
        return target.count - lis.count
    }
}
