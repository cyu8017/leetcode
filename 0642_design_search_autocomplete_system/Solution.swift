// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

class AutocompleteSystem {
    private var counts = [String: Int]()
    private var current = ""

    init(_ sentences: [String], _ times: [Int]) {
        for i in 0..<sentences.count {
            counts[sentences[i], default: 0] += times[i]
        }
    }

    func input(_ c: Character) -> [String] {
        if c == "#" {
            counts[current, default: 0] += 1
            current = ""
            return []
        }
        current.append(c)
        let prefix = current
        var matches = counts.keys.filter { $0.hasPrefix(prefix) }
        matches.sort {
            let ca = counts[$0]!, cb = counts[$1]!
            if ca != cb { return ca > cb }
            return $0 < $1
        }
        return Array(matches.prefix(3))
    }
}
