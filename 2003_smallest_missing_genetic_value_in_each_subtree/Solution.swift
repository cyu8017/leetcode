// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

class Solution {
    func smallestMissingValueSubtree(_ parents: [Int], _ nums: [Int]) -> [Int] {
        let n = parents.count
        var children = [[Int]](repeating: [], count: n)
        for i in 1..<n { children[parents[i]].append(i) }
        var ans = [Int](repeating: 1, count: n)
        guard let one = nums.firstIndex(of: 1) else { return ans }
        var seen = Set<Int>()
        func collect(_ u: Int) {
            if seen.contains(nums[u]) { return }
            seen.insert(nums[u])
            for v in children[u] { collect(v) }
        }
        var miss = 1, node = one, prev = -1
        while node != -1 {
            for v in children[node] where v != prev { collect(v) }
            seen.insert(nums[node])
            while seen.contains(miss) { miss += 1 }
            ans[node] = miss
            prev = node
            node = parents[node]
        }
        return ans
    }
}
