// LeetCode 2170 - Minimum Operations to Make the Array Alternating
// https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        let n = nums.count
        if n == 1 { return 0 }
        func top2(_ idxs: [Int]) -> (Int, Int, Int, Int) {
            var freq = [Int: Int]()
            for i in idxs { freq[nums[i], default: 0] += 1 }
            var a = 0, ac = 0, b = 0, bc = 0
            for (v, c) in freq {
                if c > ac { b = a; bc = ac; a = v; ac = c }
                else if c > bc { b = v; bc = c }
            }
            return (a, ac, b, bc)
        }
        let even = (0..<n).filter { $0 % 2 == 0 }
        let odd = (0..<n).filter { $0 % 2 == 1 }
        let e = top2(even), o = top2(odd)
        if e.0 != o.0 { return n - e.1 - o.1 }
        return min(n - e.1 - o.3, n - e.3 - o.1)
    }
}
