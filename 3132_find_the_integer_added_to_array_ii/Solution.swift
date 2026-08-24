// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

class Solution {
    func minimumAddedInteger(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let a = nums1.sorted(), b = nums2.sorted()
        var ans = 1 << 30
        for t in 0..<3 {
            let x = b[0] - a[t]
            if ok(a, b, x) { ans = min(ans, x) }
        }
        return ans
    }

    private func ok(_ nums1: [Int], _ nums2: [Int], _ x: Int) -> Bool {
        var i = 0, j = 0, cnt = 0
        while i < nums1.count && j < nums2.count {
            if nums2[j] - nums1[i] != x { cnt += 1 }
            else { j += 1 }
            i += 1
        }
        return cnt <= 2
    }
}
