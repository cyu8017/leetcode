// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

class Solution {
    func pyramidTransition(_ bottom: String, _ allowed: [String]) -> Bool {
        var transitions = [String: [Character]]()
        for triple in allowed {
            let key = String(triple.prefix(2))
            transitions[key, default: []].append(triple.last!)
        }
        var memo = [String: Bool]()
        func dfs(_ row: String) -> Bool {
            if row.count == 1 { return true }
            if let cached = memo[row] { return cached }
            var options = [[Character]]()
            let chars = Array(row)
            for i in 0..<(chars.count - 1) {
                let key = String(chars[i...i+1])
                guard let opts = transitions[key] else { memo[row] = false; return false }
                options.append(opts)
            }
            var path = [Character]()
            func build(_ index: Int) -> Bool {
                if index == options.count { return dfs(String(path)) }
                for ch in options[index] {
                    path.append(ch)
                    if build(index + 1) { return true }
                    path.removeLast()
                }
                return false
            }
            let ok = build(0)
            memo[row] = ok
            return ok
        }
        return dfs(bottom)
    }
}
