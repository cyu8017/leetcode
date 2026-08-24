// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

protocol CategoryHandler {
    func haveSameCategory(_ a: Int, _ b: Int) -> Bool
}

class Solution {
    func numberOfCategories(_ n: Int, _ categoryHandler: CategoryHandler) -> Int {
        var parent = Array(0..<n)
        func find(_ x0: Int) -> Int {
            var x = x0
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        for i in 0..<n {
            for j in (i + 1)..<n where categoryHandler.haveSameCategory(i, j) {
                let a = find(i), b = find(j)
                if a != b { parent[a] = b }
            }
        }
        var ans = 0
        for i in 0..<n where find(i) == i { ans += 1 }
        return ans
    }
}
