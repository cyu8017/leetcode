// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution {
    func createSortedArray(_ instructions: [Int]) -> Int {
        let MOD = 1_000_000_007
        let size = (instructions.max() ?? 0) + 2
        var bit = [Int](repeating: 0, count: size + 1)
        func query(_ i: Int) -> Int {
            var i = i, s = 0
            while i > 0 {
                s += bit[i]
                i -= i & -i
            }
            return s
        }
        func update(_ i: Int) {
            var i = i
            while i <= size {
                bit[i] += 1
                i += i & -i
            }
        }
        var ans = 0
        for (i, x) in instructions.enumerated() {
            ans = (ans + min(query(x - 1), i - query(x))) % MOD
            update(x)
        }
        return ans
    }
}
