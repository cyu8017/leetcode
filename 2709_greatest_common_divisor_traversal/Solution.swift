// LeetCode 2709 - Greatest Common Divisor Traversal
// https://leetcode.com/problems/greatest-common-divisor-traversal/

class Solution {
    private var parent: [Int] = []

    func canTraverseAllPairs(_ nums: [Int]) -> Bool {
        let n = nums.count
        if n == 1 { return true }
        let mx = nums.max() ?? 0
        parent = Array(0...mx)
        var has = Array(repeating: false, count: mx + 1)
        for x in nums {
            if x == 1 { return false }
            has[x] = true
        }
        var sieve = Array(repeating: 0, count: mx + 1)
        if mx >= 2 {
            for i in 2...mx {
                if sieve[i] == 0 {
                    var j = i
                    while j <= mx {
                        if sieve[j] == 0 { sieve[j] = i }
                        if has[j] { unite(i, j) }
                        j += i
                    }
                }
            }
        }
        let root = find(nums[0])
        for x in nums where find(x) != root { return false }
        return true
    }

    private func find(_ x: Int) -> Int {
        if parent[x] != x { parent[x] = find(parent[x]) }
        return parent[x]
    }

    private func unite(_ a: Int, _ b: Int) {
        let ra = find(a), rb = find(b)
        if ra != rb { parent[ra] = rb }
    }
}
