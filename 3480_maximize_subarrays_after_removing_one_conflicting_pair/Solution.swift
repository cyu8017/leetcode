// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

class Solution {
    func maxSubarrays(_ n: Int, _ conflictingPairs: [[Int]]) -> Int {
        let m = conflictingPairs.count
        var best = 0
        for skip in 0..<m {
            var rightLimit = Array(repeating: n + 1, count: n + 2)
            for i in 0..<m where i != skip {
                var a = conflictingPairs[i][0], b = conflictingPairs[i][1]
                if a > b { swap(&a, &b) }
                if b < rightLimit[a] { rightLimit[a] = b }
            }
            var minRight = n + 1
            var cnt = 0
            for l in stride(from: n, through: 1, by: -1) {
                if rightLimit[l] < minRight { minRight = rightLimit[l] }
                cnt += minRight - l
            }
            if cnt > best { best = cnt }
        }
        return best
    }
}
