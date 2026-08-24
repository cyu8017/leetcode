// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

private class BIT {
    let n: Int
    var c: [Int]
    init(_ n: Int) {
        self.n = n
        self.c = Array(repeating: 0, count: n + 1)
    }
    func update(_ x: Int, _ delta: Int) {
        var i = x
        while i <= n {
            c[i] += delta
            i += i & -i
        }
    }
    func query(_ x: Int) -> Int {
        var i = x, s = 0
        while i > 0 {
            s += c[i]
            i -= i & -i
        }
        return s
    }
}

class Solution {
    func countOfPeaks(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        var a = nums
        let n = a.count
        let tree = BIT(n - 1)
        for i in 1..<(n - 1) { updatePeak(&a, tree, n, i, 1) }
        var ans: [Int] = []
        for q in queries {
            if q[0] == 1 {
                let l = q[1] + 1, r = q[2] - 1
                ans.append(l <= r ? tree.query(r) - tree.query(l - 1) : 0)
            } else {
                let idx = q[1], val = q[2]
                for i in (idx - 1)...(idx + 1) { updatePeak(&a, tree, n, i, -1) }
                a[idx] = val
                for i in (idx - 1)...(idx + 1) { updatePeak(&a, tree, n, i, 1) }
            }
        }
        return ans
    }

    private func updatePeak(_ nums: inout [Int], _ tree: BIT, _ n: Int, _ i: Int, _ val: Int) {
        if i <= 0 || i >= n - 1 { return }
        if nums[i - 1] < nums[i] && nums[i] > nums[i + 1] { tree.update(i, val) }
    }
}
