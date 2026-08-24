// LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
// https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

class Solution {
    func minEliminationTime(_ timeReq: [Int], _ splitTime: Int) -> Int {
        var pq = timeReq.sorted()
        while pq.count > 1 {
            pq.removeFirst()
            let x = pq.removeFirst()
            let v = x + splitTime
            var lo = 0, hi = pq.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if pq[mid] < v { lo = mid + 1 } else { hi = mid }
            }
            pq.insert(v, at: lo)
        }
        return pq[0]
    }
}
