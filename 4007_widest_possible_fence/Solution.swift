// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/


class Solution {
    func maximumWidth(_ planks: [Int]) -> Int {
        var cnt = [Int: Int]()
        for x in planks { cnt[x, default: 0] += 1 }
        var t = [Int: Int]()
        var ans = 0
        for (x, v1) in cnt {
            t[x, default: 0] += v1
            ans = max(ans, t[x]!)
            t[x * 2, default: 0] += v1 / 2
            ans = max(ans, t[x * 2]!)
            for (y, v2) in cnt {
                if y > x {
                    let key = x + y
                    t[key, default: 0] += min(v1, v2)
                    ans = max(ans, t[key]!)
                }
            }
        }
        return ans
    }
}
