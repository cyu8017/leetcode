// LeetCode 3468 - Find the Number of Copy Arrays
// https://leetcode.com/problems/find-the-number-of-copy-arrays/

class Solution {
    func countArrays(_ original: [Int], _ bounds: [[Int]]) -> Int {
        let n = original.count
        var lo = bounds[0][0], hi = bounds[0][1]
        if n >= 2 {
            for i in 1..<n {
                let diff = original[i] - original[i - 1]
                let lo2 = bounds[i][0], hi2 = bounds[i][1]
                var nlo = lo + diff, nhi = hi + diff
                if nlo < lo2 { nlo = lo2 }
                if nhi > hi2 { nhi = hi2 }
                if nlo > nhi { return 0 }
                lo = nlo
                hi = nhi
            }
        }
        return hi - lo + 1
    }
}
