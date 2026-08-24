// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

class Solution {
    func maximumSetSize(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let s1 = Set(nums1), s2 = Set(nums2)
        var a = 0, b = 0, c = 0
        for x in s1 where !s2.contains(x) { a += 1 }
        for x in s2 {
            if !s1.contains(x) { b += 1 }
            else { c += 1 }
        }
        let n = nums1.count
        a = min(a, n / 2)
        b = min(b, n / 2)
        return min(a + b + c, n)
    }
}
