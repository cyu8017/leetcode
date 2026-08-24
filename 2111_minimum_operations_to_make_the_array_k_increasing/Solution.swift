// LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

class Solution {
    func kIncreasing(_ arr: [Int], _ k: Int) -> Int {
        var ans = 0
        let n = arr.count
        for start in 0..<k {
            var seq = [Int]()
            var i = start
            while i < n { seq.append(arr[i]); i += k }
            var tails = [Int]()
            for x in seq {
                var lo = 0, hi = tails.count
                while lo < hi {
                    let mid = (lo + hi) / 2
                    if tails[mid] <= x { lo = mid + 1 }
                    else { hi = mid }
                }
                if lo == tails.count { tails.append(x) }
                else { tails[lo] = x }
            }
            ans += seq.count - tails.count
        }
        return ans
    }
}
