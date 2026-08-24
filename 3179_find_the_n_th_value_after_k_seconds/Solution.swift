// LeetCode 3179 - Find the N-th Value After K Seconds
// https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

class Solution {
    func valueAfterKSeconds(_ n: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        var a = Array(repeating: 1, count: n)
        for _ in 0..<k {
            for i in 1..<n { a[i] = (a[i] + a[i - 1]) % mod }
        }
        return a[n - 1]
    }
}
