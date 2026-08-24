// LeetCode 2835 - Minimum Operations to Form Subsequence With Target Sum
// https://leetcode.com/problems/minimum-operations-to-form-subsequence-with-target-sum/

class Solution {
    func minOperations(_ nums: [Int], _ target: Int) -> Int {
        var cnt = Array(repeating: 0, count: 32)
        var sum = 0
        for v in nums {
            sum += v
            var b = 0
            while (1 << b) < v { b += 1 }
            cnt[b] += 1
        }
        if sum < target { return -1 }
        var ans = 0
        for i in 0..<31 {
            if (target & (1 << i)) != 0 {
                if cnt[i] > 0 {
                    cnt[i] -= 1
                } else {
                    var j = i + 1
                    while j < 32 && cnt[j] == 0 { j += 1 }
                    if j == 32 { return -1 }
                    while j > i {
                        cnt[j] -= 1
                        cnt[j - 1] += 2
                        ans += 1
                        j -= 1
                    }
                    cnt[i] -= 1
                }
            }
            cnt[i + 1] += cnt[i] / 2
        }
        return ans
    }
}
