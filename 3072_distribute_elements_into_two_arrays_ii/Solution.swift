// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

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
    func resultArray(_ nums: [Int]) -> [Int] {
        var st = nums.sorted()
        let n = st.count
        let tree1 = BIT(n + 1)
        let tree2 = BIT(n + 1)
        var arr1 = [nums[0]]
        var arr2 = [nums[1]]
        tree1.update(idx(st, nums[0]), 1)
        tree2.update(idx(st, nums[1]), 1)
        for i in 2..<nums.count {
            let x = nums[i]
            let id = idx(st, x)
            let a = arr1.count - tree1.query(id)
            let b = arr2.count - tree2.query(id)
            if a > b || (a == b && arr1.count <= arr2.count) {
                arr1.append(x)
                tree1.update(id, 1)
            } else {
                arr2.append(x)
                tree2.update(id, 1)
            }
        }
        return arr1 + arr2
    }

    private func idx(_ st: [Int], _ x: Int) -> Int {
        var lo = 0, hi = st.count
        while lo < hi {
            let mid = (lo + hi) / 2
            if st[mid] < x { lo = mid + 1 }
            else { hi = mid }
        }
        return lo + 1
    }
}
