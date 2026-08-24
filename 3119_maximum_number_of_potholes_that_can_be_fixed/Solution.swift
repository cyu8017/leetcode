// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

class Solution {
    func maxPotholes(_ road: String, _ budget: Int) -> Int {
        let road = road + "."
        let n = road.count
        var cnt = Array(repeating: 0, count: n)
        var k = 0, ans = 0
        for c in road {
            if c == "x" { k += 1 }
            else if k > 0 {
                cnt[k] += 1
                k = 0
            }
        }
        var rem = budget
        k = n - 1
        while k > 0 && rem > 0 {
            let t = min(rem / (k + 1), cnt[k])
            ans += t * k
            rem -= t * (k + 1)
            cnt[k - 1] += cnt[k] - t
            k -= 1
        }
        return ans
    }
}
