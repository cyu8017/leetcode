// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

class Solution {
    func twoOutOfThree(_ nums1: [Int], _ nums2: [Int], _ nums3: [Int]) -> [Int] {
        let s0 = Set(nums1), s1 = Set(nums2), s2 = Set(nums3)
        var ans = [Int]()
        for v in 1...100 {
            let c = (s0.contains(v) ? 1 : 0) + (s1.contains(v) ? 1 : 0) + (s2.contains(v) ? 1 : 0)
            if c >= 2 { ans.append(v) }
        }
        return ans
    }
}
