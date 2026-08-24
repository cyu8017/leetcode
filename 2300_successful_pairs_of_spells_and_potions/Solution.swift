// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution {
    func successfulPairs(_ spells: [Int], _ potions: [Int], _ success: Int) -> [Int] {
        let potions = potions.sorted()
        let m = potions.count
        return spells.map { spell in
            var lo = 0, hi = m
            while lo < hi {
                let mid = (lo + hi) / 2
                if spell * potions[mid] >= success { hi = mid }
                else { lo = mid + 1 }
            }
            return m - lo
        }
    }
}
