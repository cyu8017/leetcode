// LeetCode 2234 - Maximum Total Beauty of the Gardens
// https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

class Solution {
    func maximumBeauty(_ flowers: [Int], _ newFlowers: Int, _ target: Int, _ full: Int, _ partial: Int) -> Int {
        var flowers = flowers.map { min($0, target) }.sorted()
        let n = flowers.count
        let sum = flowers.reduce(0, +)
        if target * n - sum <= newFlowers { return n * full }
        var pref = [Int](repeating: 0, count: n + 1)
        for i in 0..<n { pref[i + 1] = pref[i] + flowers[i] }
        var ans = 0
        var j = n - 1
        var remain = newFlowers
        for complete in 0...n {
            if complete > 0 {
                let need = target - flowers[n - complete]
                if remain < need { break }
                remain -= need
            }
            while j >= n - complete || (j >= 0 && flowers[j] * (j + 1) - pref[j + 1] > remain) {
                j -= 1
            }
            var partialVal = 0
            if j >= 0 {
                let extra = (remain - (flowers[j] * (j + 1) - pref[j + 1])) / (j + 1)
                partialVal = flowers[j] + extra
                if partialVal >= target { partialVal = target - 1 }
            }
            ans = max(ans, complete * full + partialVal * partial)
        }
        return ans
    }
}
