// LeetCode 1387 - Sort Integers by The Power Value
// https://leetcode.com/problems/sort-integers-by-the-power-value/

class Solution {
    func getKth(_ lo: Int, _ hi: Int, _ k: Int) -> Int {
        var memo = [Int: Int]()
        func power(_ x: Int) -> Int {
            if x == 1 { return 0 }
            if let m = memo[x] { return m }
            let v = 1 + power(x % 2 == 0 ? x / 2 : 3 * x + 1)
            memo[x] = v
            return v
        }
        return Array(lo...hi).sorted { a, b in
            let pa = power(a), pb = power(b)
            return pa != pb ? pa < pb : a < b
        }[k - 1]
    }
}
