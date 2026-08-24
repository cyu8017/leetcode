// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

class Solution {
    func numberOfPairs(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        var ans = 0
        for x in nums1 {
            for y in nums2 where x % (y * k) == 0 { ans += 1 }
        }
        return ans
    }
}
