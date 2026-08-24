// LeetCode 3935 - Power Update After K-th Largest Insertion I
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/


class Solution {
    func powerUpdate(_ nums: [Int], _ p: Int, _ queries: [[Int]]) -> [Int] {
        var L = [Int: Int]()
        var R = [Int: Int]()
        func merge(_ st: inout [Int: Int], _ x: Int, _ v: Int) {
            let c = st[x, default: 0]
            if c + v == 0 { st.removeValue(forKey: x) }
            else { st[x] = c + v }
        }
        func firstKey(_ st: [Int: Int]) -> Int { st.keys.min()! }
        func lastKey(_ st: [Int: Int]) -> Int { st.keys.max()! }
        var sz1 = 0, sz2 = nums.count
        for x in nums { merge(&R, x, 1) }
        let mod = 1_000_000_007
        func qpow(_ a0: Int, _ b0: Int) -> Int {
            var a = a0 % mod, b = b0, ans = 1
            while b > 0 {
                if b & 1 != 0 { ans = ans * a % mod }
                a = a * a % mod
                b >>= 1
            }
            return ans
        }
        var ans = Array(repeating: 0, count: queries.count)
        var pCur = p
        for qi in 0..<queries.count {
            let val = queries[qi][0], k = queries[qi][1]
            merge(&R, val, 1)
            sz2 += 1
            var node = firstKey(R)
            merge(&R, node, -1)
            sz2 -= 1
            merge(&L, node, 1)
            sz1 += 1
            while sz2 < k {
                node = lastKey(L)
                merge(&L, node, -1)
                sz1 -= 1
                merge(&R, node, 1)
                sz2 += 1
            }
            while sz2 > k {
                node = firstKey(R)
                merge(&R, node, -1)
                sz2 -= 1
                merge(&L, node, 1)
                sz1 += 1
            }
            let x = firstKey(R)
            pCur = qpow(pCur, x)
            ans[qi] = pCur
        }
        return ans
    }
}
