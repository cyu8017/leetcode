// LeetCode 0668 - Kth Smallest Number in Multiplication Table
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

class Solution {
    func findKthNumber(_ m: Int, _ n: Int, _ k: Int) -> Int {
        var lo = 1, hi = m * n
        while lo < hi {
            let mid = lo + (hi - lo) / 2
            if countLe(m, n, mid) >= k { hi = mid } else { lo = mid + 1 }
        }
        return lo
    }

    private func countLe(_ m: Int, _ n: Int, _ x: Int) -> Int {
        var count = 0
        for row in 1...m { count += min(x / row, n) }
        return count
    }
}
