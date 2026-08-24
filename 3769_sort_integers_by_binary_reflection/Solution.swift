// LeetCode 3769 - Sort Integers By Binary Reflection
// https://leetcode.com/problems/sort-integers-by-binary-reflection/

class Solution {
    func sortByReflection(_ nums: [Int]) -> [Int] {
        return nums.sorted { a, b in
            let fa = f(a), fb = f(b)
            if fa != fb { return fa < fb }
            return a < b
        }
    }

    private func f(_ x: Int) -> Int {
        var x = x, y = 0
        while x != 0 {
            y = (y << 1) | (x & 1)
            x >>= 1
        }
        return y
    }
}
