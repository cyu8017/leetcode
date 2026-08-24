// LeetCode 2525 - Categorize Box According to Criteria
// https://leetcode.com/problems/categorize-box-according-to-criteria/

class Solution {
    func categorizeBox(_ length: Int, _ width: Int, _ height: Int, _ mass: Int) -> String {
        let bulky = length >= 10000 || width >= 10000 || height >= 10000
            || length * width * height >= 1_000_000_000
        let heavy = mass >= 100
        if bulky && heavy { return "Both" }
        if bulky { return "Bulky" }
        if heavy { return "Heavy" }
        return "Neither"
    }
}
