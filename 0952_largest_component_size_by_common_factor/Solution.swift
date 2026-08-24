// LeetCode 0952 - Largest Component Size by Common Factor
// https://leetcode.com/problems/largest-component-size-by-common-factor/

class Solution {
    func largestComponentSize(_ nums: [Int]) -> Int {
        let mx = nums.max() ?? 0
        var parent = Array(0...mx)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        func unite(_ a: Int, _ b: Int) { parent[find(a)] = find(b) }
        func factors(_ x: Int) -> [Int] {
            var x = x, res = [Int]()
            var d = 2
            while d * d <= x {
                if x % d == 0 {
                    res.append(d)
                    while x % d == 0 { x /= d }
                }
                d += 1
            }
            if x > 1 { res.append(x) }
            return res
        }
        for num in nums {
            for f in factors(num) { unite(num, f) }
        }
        var cnt = [Int: Int]()
        var ans = 0
        for num in nums {
            let r = find(num)
            cnt[r, default: 0] += 1
            ans = max(ans, cnt[r]!)
        }
        return ans
    }
}
