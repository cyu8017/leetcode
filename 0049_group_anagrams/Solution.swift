// LeetCode 0049 - Group Anagrams
// https://leetcode.com/problems/group-anagrams/

class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var groups: [String: [String]] = [:]

        for word in strs {
            let key = String(word.sorted())
            groups[key, default: []].append(word)
        }

        var result = groups.values.map { $0.sorted() }
        result.sort { minGroupIndex(strs, $0) > minGroupIndex(strs, $1) }
        return result
    }

    private func minGroupIndex(_ strs: [String], _ group: [String]) -> Int {
        var min = strs.count
        for word in group {
            if let index = strs.firstIndex(of: word) {
                min = Swift.min(min, index)
            }
        }
        return min
    }
}
