// LeetCode 2625 - Flatten Deeply Nested Array
// https://leetcode.com/problems/flatten-deeply-nested-array/

enum NestedInteger {
    case num(Int)
    case list([NestedInteger])
}

class Solution {
    func flat(_ arr: [NestedInteger], _ n: Int) -> [NestedInteger] {
        var out: [NestedInteger] = []
        func dfs(_ items: [NestedInteger], _ depth: Int) {
            for item in items {
                switch item {
                case .num:
                    out.append(item)
                case .list(let nested):
                    if depth < n {
                        dfs(nested, depth + 1)
                    } else {
                        out.append(item)
                    }
                }
            }
        }
        dfs(arr, 0)
        return out
    }

    func flat(_ arr: [Int], _ n: Int) -> [Int] {
        arr
    }
}
