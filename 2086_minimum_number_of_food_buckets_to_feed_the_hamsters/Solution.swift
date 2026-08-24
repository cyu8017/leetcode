// LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
// https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/

class Solution {
    func minimumBuckets(_ hamsters: String) -> Int {
        var b = Array(hamsters)
        var ans = 0
        for i in 0..<b.count {
            if b[i] != "H" { continue }
            if i > 0 && b[i - 1] == "B" { continue }
            if i + 1 < b.count && b[i + 1] == "." {
                b[i + 1] = "B"
                ans += 1
            } else if i > 0 && b[i - 1] == "." {
                b[i - 1] = "B"
                ans += 1
            } else {
                return -1
            }
        }
        return ans
    }
}
