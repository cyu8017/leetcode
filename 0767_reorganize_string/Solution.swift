// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

class Solution {
    func reorganizeString(_ s: String) -> String {
        var counts = [Character: Int]()
        for ch in s { counts[ch, default: 0] += 1 }
        var items = counts.map { ($0.key, $0.value) }.sorted { $0.1 > $1.1 }
        if items[0].1 > (s.count + 1) / 2 { return "" }
        var result = Array(repeating: Character(" "), count: s.count)
        var idx = 0
        for (ch, cnt) in items {
            for _ in 0..<cnt {
                if idx >= s.count { idx = 1 }
                result[idx] = ch
                idx += 2
            }
        }
        return String(result)
    }
}
