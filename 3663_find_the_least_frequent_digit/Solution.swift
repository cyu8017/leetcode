// LeetCode 3663 - Find The Least Frequent Digit
// https://leetcode.com/problems/find-the-least-frequent-digit/

class Solution {
    func getLeastFrequentDigit(_ n: Int) -> Int {
        var n = n
        var cnt = Array(repeating: 0, count: 10)
        var ans = 0, f = 1 << 30
        while n > 0 { cnt[n % 10] += 1; n /= 10 }
        for x in 0..<10 {
            if cnt[x] > 0 && cnt[x] < f {
                f = cnt[x]
                ans = x
            }
        }
        return ans
    }
}
