// LeetCode 1361 - Validate Binary Tree Nodes
// https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution {
    func validateBinaryTreeNodes(_ n: Int, _ leftChild: [Int], _ rightChild: [Int]) -> Bool {
        var indeg = Array(repeating: 0, count: n)
        for x in leftChild + rightChild where x != -1 {
            indeg[x] += 1
            if indeg[x] > 1 { return false }
        }
        let roots = indeg.indices.filter { indeg[$0] == 0 }
        if roots.count != 1 { return false }
        var seen = Set<Int>()
        var st = roots
        while !st.isEmpty {
            let u = st.removeLast()
            if seen.contains(u) { return false }
            seen.insert(u)
            for v in [leftChild[u], rightChild[u]] where v != -1 { st.append(v) }
        }
        return seen.count == n
    }
}
