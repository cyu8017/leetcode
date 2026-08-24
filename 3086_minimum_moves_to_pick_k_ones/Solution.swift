// LeetCode 3086 - Minimum Moves to Pick K Ones
// https://leetcode.com/problems/minimum-moves-to-pick-k-ones/

class Solution {
    func minimumMoves(_ nums: [Int], _ k: Int, _ maxChanges: Int) -> Int {
        let n = nums.count
        var cnt = Array(repeating: 0, count: n + 1)
        var s = Array(repeating: 0, count: n + 1)
        for i in 1...n {
            cnt[i] = cnt[i - 1] + nums[i - 1]
            s[i] = s[i - 1] + i * nums[i - 1]
        }
        var ans = Int.max
        for i in 1...n {
            var t = 0
            var need = k - nums[i - 1]
            for j in [i - 1, i + 1] {
                if need > 0 && 1 <= j && j <= n && nums[j - 1] == 1 {
                    need -= 1
                    t += 1
                }
            }
            let c = min(need, maxChanges)
            need -= c
            t += c * 2
            if need <= 0 {
                ans = min(ans, t)
                continue
            }
            var l = 2, r = max(i - 1, n - i)
            while l <= r {
                let mid = (l + r) >> 1
                let l1 = max(1, i - mid), r1 = max(0, i - 2)
                let l2 = min(n + 1, i + 2), r2 = min(n, i + mid)
                let c1 = r1 >= l1 ? cnt[r1] - cnt[l1 - 1] : 0
                let c2 = r2 >= l2 ? cnt[r2] - cnt[l2 - 1] : 0
                if c1 + c2 >= need {
                    let t1 = c1 * i - (s[r1] - s[l1 - 1])
                    let t2 = s[r2] - s[l2 - 1] - c2 * i
                    ans = min(ans, t + t1 + t2)
                    r = mid - 1
                } else {
                    l = mid + 1
                }
            }
        }
        return ans
    }
}
