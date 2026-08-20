// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

class Solution {
    func suggestedProducts(_ products: [String], _ searchWord: String) -> [[String]] {
        let sorted = products.sorted()
        var ans: [[String]] = []
        var prefix = ""
        for ch in searchWord {
            prefix.append(ch)
            var lo = 0, hi = sorted.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if sorted[mid] < prefix { lo = mid + 1 } else { hi = mid }
            }
            var group: [String] = []
            for i in lo..<min(lo + 3, sorted.count) {
                if sorted[i].hasPrefix(prefix) { group.append(sorted[i]) } else { break }
            }
            ans.append(group)
        }
        return ans
    }
}
