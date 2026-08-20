// LeetCode 1385 - Find the Distance Value Between Two Arrays
// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution {
    func findTheDistanceValue(_ arr1: [Int], _ arr2: [Int], _ d: Int) -> Int {
        let b = arr2.sorted()
        var ans = 0
        for x in arr1 {
            var lo = 0, hi = b.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if b[mid] < x { lo = mid + 1 } else { hi = mid }
            }
            let okLeft = lo == 0 || abs(b[lo - 1] - x) > d
            let okRight = lo == b.count || abs(b[lo] - x) > d
            if okLeft && okRight { ans += 1 }
        }
        return ans
    }
}
