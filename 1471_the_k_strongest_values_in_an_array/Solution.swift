// LeetCode 1471 - The k Strongest Values in an Array
// https://leetcode.com/problems/the-k-strongest-values-in-an-array/

class Solution {
    func getStrongest(_ arr: [Int], _ k: Int) -> [Int] {
        var arr = arr.sorted()
        let median = arr[(arr.count - 1) / 2]
        arr.sort { a, b in
            let da = abs(a - median), db = abs(b - median)
            return da != db ? da > db : a > b
        }
        return Array(arr.prefix(k))
    }
}
