// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

class Solution {
    func mincostToHireWorkers(_ quality: [Int], _ wage: [Int], _ k: Int) -> Double {
        let workers = zip(wage, quality).map { (Double($0) / Double($1), $1) }.sorted { $0.0 < $1.0 }
        var heap = [Int]()
        var totalQ = 0
        var ans = Double.greatestFiniteMagnitude
        for w in workers {
            let q = w.1
            heap.append(q)
            totalQ += q
            heap.sort()
            if heap.count > k {
                totalQ -= heap.removeLast()
            }
            if heap.count == k {
                ans = min(ans, Double(totalQ) * w.0)
            }
        }
        return ans
    }
}
