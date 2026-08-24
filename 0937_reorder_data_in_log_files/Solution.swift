// LeetCode 0937 - Reorder Data in Log Files
// https://leetcode.com/problems/reorder-data-in-log-files/

class Solution {
    func reorderLogFiles(_ logs: [String]) -> [String] {
        var letter = [String]()
        var digit = [String]()
        for log in logs {
            let sp = log.firstIndex(of: " ")!
            let restStart = log.index(after: sp)
            if log[restStart].isLetter { letter.append(log) }
            else { digit.append(log) }
        }
        letter.sort { a, b in
            let spa = a.firstIndex(of: " ")!
            let spb = b.firstIndex(of: " ")!
            let resta = a[a.index(after: spa)...]
            let restb = b[b.index(after: spb)...]
            if resta != restb { return resta < restb }
            return a[..<spa] < b[..<spb]
        }
        return letter + digit
    }
}
