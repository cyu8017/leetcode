// LeetCode 0364 - Nested List Weight Sum II
// https://leetcode.com/problems/nested-list-weight-sum-ii/

class NestedInteger {
    private var integer: Int?
    private var list: [NestedInteger] = []

    init(_ value: Int) {
        self.integer = value
    }

    init() {}

    func isInteger() -> Bool {
        integer != nil
    }

    func getInteger() -> Int {
        integer ?? 0
    }

    func getList() -> [NestedInteger] {
        list
    }

    func add(_ item: NestedInteger) {
        list.append(item)
    }
}

class Solution {
    func depthSum(_ nestedList: [NestedInteger]) -> Int {
        var weighted: [(Int, Int)] = []

        func dfs(_ items: [NestedInteger], _ depth: Int) {
            for item in items {
                if item.isInteger() {
                    weighted.append((item.getInteger(), depth))
                } else {
                    dfs(item.getList(), depth + 1)
                }
            }
        }

        dfs(nestedList, 1)
        if weighted.isEmpty {
            return 0
        }

        let maxDepth = weighted.map(\.1).max() ?? 0
        return weighted.reduce(0) { total, pair in
            total + pair.0 * (maxDepth - pair.1 + 1)
        }
    }
}
