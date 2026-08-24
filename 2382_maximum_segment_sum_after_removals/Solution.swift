// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

class Solution {
    func maximumSegmentSum(_ nums: [Int], _ removeQueries: [Int]) -> [Int] {
        let n = nums.count
        var parent = Array(0..<n)
        var sum = [Int](repeating: 0, count: n)
        var active = [Bool](repeating: false, count: n)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        func unite(_ a: Int, _ b: Int) {
            let ra = find(a), rb = find(b)
            if ra == rb { return }
            parent[rb] = ra
            sum[ra] += sum[rb]
        }
        var ans = [Int](repeating: 0, count: n)
        var best = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            ans[i] = best
            let idx = removeQueries[i]
            active[idx] = true
            sum[idx] = nums[idx]
            if idx > 0 && active[idx - 1] { unite(idx, idx - 1) }
            if idx + 1 < n && active[idx + 1] { unite(idx, idx + 1) }
            best = max(best, sum[find(idx)])
        }
        return ans
    }
}
