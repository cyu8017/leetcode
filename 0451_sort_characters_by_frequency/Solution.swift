// LeetCode 0451 - Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

class Solution {
    func frequencySort(_ s: String) -> String {
        var counts: [Character: Int] = [:]
        for ch in s {
            counts[ch, default: 0] += 1
        }

        let ordered = counts.sorted {
            if $0.value != $1.value {
                return $0.value > $1.value
            }
            return $0.key < $1.key
        }

        var result = ""
        for (ch, count) in ordered {
            result += String(repeating: String(ch), count: count)
        }
        return result
    }
}
