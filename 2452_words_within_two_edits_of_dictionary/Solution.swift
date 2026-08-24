// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Solution {
    func twoEditWords(_ queries: [String], _ dictionary: [String]) -> [String] {
        var ans = [String]()
        let dicts = dictionary.map { Array($0) }
        for q in queries {
            let qc = Array(q)
            var ok = false
            for d in dicts {
                var diff = 0
                for i in 0..<qc.count {
                    if qc[i] != d[i] {
                        diff += 1
                        if diff > 2 { break }
                    }
                }
                if diff <= 2 { ok = true; break }
            }
            if ok { ans.append(q) }
        }
        return ans
    }
}
