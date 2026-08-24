// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

class Solution {
    func beautifulSubsets(_ nums: [Int], _ k: Int) -> Int {
        var freq = [Int: Int]()
        for x in nums { freq[x, default: 0] += 1 }
        var groups = [Int: [Int]]()
        for key in freq.keys {
            groups[key % k, default: []].append(key)
        }
        var ans = 1
        for var vals in groups.values {
            vals.sort()
            var prevTake = 0, prevSkip = 1
            var prevVal = Int.min / 2
            for v in vals {
                var ways = 1
                for _ in 0..<freq[v]! { ways *= 2 }
                ways -= 1
                let skip = prevTake + prevSkip
                var take = ways * prevSkip
                if prevVal + k != v { take += ways * prevTake }
                prevTake = take
                prevSkip = skip
                prevVal = v
            }
            ans *= prevTake + prevSkip
        }
        return ans - 1
    }
}
