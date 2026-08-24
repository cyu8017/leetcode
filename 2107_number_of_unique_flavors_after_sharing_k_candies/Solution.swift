// LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
// https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

class Solution {
    func shareCandies(_ candies: [Int], _ k: Int) -> Int {
        var freq = [Int: Int]()
        for c in candies { freq[c, default: 0] += 1 }
        if k == 0 { return freq.count }
        for i in 0..<k {
            let c = candies[i]
            freq[c]! -= 1
            if freq[c] == 0 { freq.removeValue(forKey: c) }
        }
        var ans = freq.count
        for i in k..<candies.count {
            freq[candies[i - k], default: 0] += 1
            let c = candies[i]
            freq[c]! -= 1
            if freq[c] == 0 { freq.removeValue(forKey: c) }
            ans = max(ans, freq.count)
        }
        return ans
    }
}
