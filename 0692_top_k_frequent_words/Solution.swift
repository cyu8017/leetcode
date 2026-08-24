// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

class Solution {
    func topKFrequent(_ words: [String], _ k: Int) -> [String] {
        var freq = [String: Int]()
        for w in words { freq[w, default: 0] += 1 }
        return freq.keys.sorted {
            let fa = freq[$0]!, fb = freq[$1]!
            if fa != fb { return fa > fb }
            return $0 < $1
        }.prefix(k).map { $0 }
    }
}
