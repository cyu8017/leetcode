// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

class Solution {
    func countComponents(_ nums: [Int], _ threshold: Int) -> Int {
        let n = nums.count
        var parent = Array(0..<n)
        func find(_ x: Int) -> Int {
            if parent[x] != x { parent[x] = find(parent[x]) }
            return parent[x]
        }
        func unite(_ a: Int, _ b: Int) {
            let ra = find(a), rb = find(b)
            if ra != rb { parent[ra] = rb }
        }
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        var idx = [Int: Int]()
        for i in 0..<n { idx[nums[i]] = i }
        if threshold >= 1 {
            for d in 1...threshold {
                var first = -1
                var m = d
                while m <= threshold {
                    if let i = idx[m] {
                        if first == -1 { first = i }
                        else if nums[first] / gcd(nums[first], nums[i]) * nums[i] <= threshold {
                            unite(first, i)
                        }
                    }
                    m += d
                }
            }
        }
        for i in 0..<n {
            for j in (i + 1)..<n {
                let a = nums[i], b = nums[j]
                let g = gcd(a, b)
                if a / g * b <= threshold { unite(i, j) }
            }
        }
        return Set((0..<n).map { find($0) }).count
    }
}
