// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

class Solution {
    func numSpecialEquivGroups(_ words: [String]) -> Int {
        var groups = Set<String>()
        for w in words {
            var even = [Character]()
            var odd = [Character]()
            for (i, ch) in w.enumerated() {
                if i % 2 == 0 { even.append(ch) }
                else { odd.append(ch) }
            }
            groups.insert(String(even.sorted()) + "|" + String(odd.sorted()))
        }
        return groups.count
    }
}
