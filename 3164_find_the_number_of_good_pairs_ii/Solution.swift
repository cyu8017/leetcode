// LeetCode 3164 - Find the Number of Good Pairs II
// https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

class Solution {
    func numberOfPairs(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        var cnt1: [Int: Int] = [:]
        for x in nums1 where x % k == 0 { cnt1[x / k, default: 0] += 1 }
        if cnt1.isEmpty { return 0 }
        var cnt2: [Int: Int] = [:]
        for x in nums2 { cnt2[x, default: 0] += 1 }
        let mx = cnt1.keys.max()!
        var ans = 0
        for (x, v) in cnt2 {
            var s = 0
            var y = x
            while y <= mx {
                if let c = cnt1[y] { s += c }
                y += x
            }
            ans += s * v
        }
        return ans
    }
}
