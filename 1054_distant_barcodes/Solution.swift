// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

class Solution {
    func rearrangeBarcodes(_ barcodes: [Int]) -> [Int] {
        var count: [Int: Int] = [:]
        for b in barcodes {
            count[b, default: 0] += 1
        }
        let n = barcodes.count
        var ans = Array(repeating: 0, count: n)
        var i = 0
        let ordered = count.sorted { $0.value > $1.value }
        for (value, freq) in ordered {
            for _ in 0..<freq {
                ans[i] = value
                i += 2
                if i >= n {
                    i = 1
                }
            }
        }
        return ans
    }
}
