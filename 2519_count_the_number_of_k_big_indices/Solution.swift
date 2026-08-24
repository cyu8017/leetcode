// LeetCode 2519 - Count the Number of K-Big Indices
// https://leetcode.com/problems/count-the-number-of-k-big-indices/

class Solution {
    func kBigIndices(_ nums: [Int], _ k: Int) -> Int {
        class Fenwick {
            var bit: [Int]
            init(_ n: Int) { bit = [Int](repeating: 0, count: n + 2) }
            func add(_ i: Int, _ v: Int) {
                var i = i
                while i < bit.count {
                    bit[i] += v
                    i += i & -i
                }
            }
            func sum(_ i: Int) -> Int {
                var i = i, s = 0
                while i > 0 {
                    s += bit[i]
                    i -= i & -i
                }
                return s
            }
        }
        let n = nums.count
        var uniq = Array(Set(nums)).sorted()
        var rank = [Int: Int]()
        for i in 0..<uniq.count { rank[uniq[i]] = i + 1 }
        let m = uniq.count
        var left = [Int](repeating: 0, count: n)
        var right = [Int](repeating: 0, count: n)
        var ft = Fenwick(m)
        for i in 0..<n {
            let r = rank[nums[i]]!
            left[i] = ft.sum(r - 1)
            ft.add(r, 1)
        }
        ft = Fenwick(m)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let r = rank[nums[i]]!
            right[i] = ft.sum(r - 1)
            ft.add(r, 1)
        }
        var ans = 0
        for i in 0..<n where left[i] >= k && right[i] >= k { ans += 1 }
        return ans
    }
}
