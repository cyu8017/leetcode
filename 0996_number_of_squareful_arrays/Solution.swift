// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

class Solution {
    func numSquarefulPerms(_ nums: [Int]) -> Int {
        var count = [Int: Int]()
        for x in nums { count[x, default: 0] += 1 }
        var graph = [Int: [Int]]()
        for a in count.keys { graph[a] = [] }
        for a in count.keys {
            for b in count.keys {
                let s = a + b
                let r = Int((Double(s)).squareRoot().rounded())
                if r * r == s { graph[a, default: []].append(b) }
            }
        }
        var ans = 0
        for x in Array(count.keys) {
            count[x]! -= 1
            dfs(x, nums.count - 1, &count, graph, &ans)
            count[x]! += 1
        }
        return ans
    }

    private func dfs(_ x: Int, _ remain: Int, _ count: inout [Int: Int], _ graph: [Int: [Int]], _ ans: inout Int) {
        if remain == 0 { ans += 1; return }
        for y in graph[x, default: []] {
            if count[y, default: 0] > 0 {
                count[y]! -= 1
                dfs(y, remain - 1, &count, graph, &ans)
                count[y]! += 1
            }
        }
    }
}
