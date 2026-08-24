// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/

class Solution {
    func pathSum(_ nums: [Int]) -> Int {
        var tree = [Int: Int]()
        var total = 0
        for num in nums {
            tree[key(num / 100, (num / 10) % 10)] = num % 10
        }
        func dfs(_ depth: Int, _ pos: Int, _ path: Int) {
            let k = key(depth, pos)
            guard let val = tree[k] else { return }
            let path = path + val
            let left = key(depth + 1, pos * 2 - 1)
            let right = key(depth + 1, pos * 2)
            if tree[left] == nil && tree[right] == nil {
                total += path
                return
            }
            dfs(depth + 1, pos * 2 - 1, path)
            dfs(depth + 1, pos * 2, path)
        }
        dfs(1, 1, 0)
        return total
    }

    private func key(_ depth: Int, _ pos: Int) -> Int { (depth << 16) | pos }
}
