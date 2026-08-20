// LeetCode 1998 - GCD Sort of an Array
// https://leetcode.com/problems/gcd-sort-of-an-array/

class Solution {
    func gcdSort(_ nums: [Int]) -> Bool {
        let m = nums.max()!
        var parent = Array(0...m)
        func find(_ x: Int) -> Int {
            var x = x
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }
        func union(_ a: Int, _ b: Int) {
            let ra = find(a), rb = find(b)
            if ra != rb { parent[rb] = ra }
        }
        var spf = Array(0...m)
        let lim = Int(Double(m).squareRoot())
        if lim >= 2 {
            for i in 2...lim {
                if spf[i] == i {
                    var j = i * i
                    while j <= m {
                        if spf[j] == j { spf[j] = i }
                        j += i
                    }
                }
            }
        }
        for x in Set(nums) {
            var y = x
            while y > 1 {
                let p = spf[y]
                union(x, p)
                while y % p == 0 { y /= p }
            }
        }
        let sortedNums = nums.sorted()
        for (a, b) in zip(nums, sortedNums) {
            if find(a) != find(b) { return false }
        }
        return true
    }
}
