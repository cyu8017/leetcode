// LeetCode 1722 - Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

class Solution {
    func minimumHammingDistance(_ source: [Int], _ target: [Int], _ allowedSwaps: [[Int]]) -> Int {
        let n = source.count
        var parent = Array(0..<n)

        func find(_ start: Int) -> Int {
            var x = start
            while parent[x] != x {
                parent[x] = parent[parent[x]]
                x = parent[x]
            }
            return x
        }

        func union(_ a: Int, _ b: Int) {
            let ra = find(a)
            let rb = find(b)
            if ra != rb {
                parent[rb] = ra
            }
        }

        for swap in allowedSwaps {
            union(swap[0], swap[1])
        }
        var groups = [Int: [Int: Int]]()
        for (i, value) in source.enumerated() {
            groups[find(i), default: [:]][value, default: 0] += 1
        }
        var ans = 0
        for (i, value) in target.enumerated() {
            let root = find(i)
            if let remaining = groups[root]?[value], remaining > 0 {
                groups[root]![value] = remaining - 1
            } else {
                ans += 1
            }
        }
        return ans
    }
}
