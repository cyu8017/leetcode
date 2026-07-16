// LeetCode 0339 - Nested List Weight Sum
// https://leetcode.com/problems/nested-list-weight-sum/

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
        var total = 0

        func dfs(_ items: [NestedInteger], _ depth: Int) {
            for item in items {
                if item.isInteger() {
                    total += item.getInteger() * depth
                } else {
                    dfs(item.getList(), depth + 1)
                }
            }
        }

        dfs(nestedList, 1)
        return total
    }
}
