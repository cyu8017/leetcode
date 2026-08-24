// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

class Solution {
    func fairCandySwap(_ aliceSizes: [Int], _ bobSizes: [Int]) -> [Int] {
        let sumA = aliceSizes.reduce(0, +)
        let sumB = bobSizes.reduce(0, +)
        let diff = (sumA - sumB) / 2
        let bob = Set(bobSizes)
        for a in aliceSizes {
            if bob.contains(a - diff) { return [a, a - diff] }
        }
        return []
    }
}
