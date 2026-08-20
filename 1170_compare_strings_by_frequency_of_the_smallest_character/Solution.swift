// LeetCode 1170 - Compare Strings by Frequency of the Smallest Character
// https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

class Solution {
    func numSmallerByFrequency(_ queries: [String], _ words: [String]) -> [Int] {
        func f(_ s: String) -> Int {
            let chars = Array(s)
            let mn = chars.min()!
            return chars.filter { $0 == mn }.count
        }
        let wf = words.map(f).sorted()
        return queries.map { q in
            let fq = f(q)
            var lo = 0, hi = wf.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if wf[mid] <= fq { lo = mid + 1 } else { hi = mid }
            }
            return wf.count - lo
        }
    }
}
