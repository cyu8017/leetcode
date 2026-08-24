// LeetCode 2195 - Append K Integers With Minimal Sum
// https://leetcode.com/problems/append-k-integers-with-minimal-sum/

class Solution {
    func minimalKSum(_ nums: [Int], _ k: Int) -> Int {
        let nums = nums.sorted()
        var ans = 0, prev = 0, k = k
        for x in nums {
            if x <= prev { continue }
            let start = prev + 1
            var end = x - 1
            if start <= end {
                var cnt = end - start + 1
                if cnt > k { end = start + k - 1; cnt = k }
                ans += (start + end) * cnt / 2
                k -= cnt
                if k == 0 { return ans }
            }
            prev = x
        }
        let s = prev + 1, e = s + k - 1
        ans += (s + e) * k / 2
        return ans
    }
}
