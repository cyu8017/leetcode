// LeetCode 2818 - Apply Operations to Maximize Score
// https://leetcode.com/problems/apply-operations-to-maximize-score/

class Solution {
    private let MOD = 1_000_000_007

    func maximumScore(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let maxV = nums.max() ?? 0
        var spf = Array(repeating: 0, count: maxV + 1)
        if maxV >= 2 {
            for i in 2...maxV where spf[i] == 0 {
                var j = i
                while j <= maxV {
                    if spf[j] == 0 { spf[j] = i }
                    j += i
                }
            }
        }
        let score = nums.map { primeScore($0, spf) }
        var left = Array(repeating: 0, count: n)
        var right = Array(repeating: 0, count: n)
        var st: [Int] = []
        for i in 0..<n {
            while !st.isEmpty && score[st.last!] < score[i] { st.removeLast() }
            left[i] = st.isEmpty ? -1 : st.last!
            st.append(i)
        }
        st.removeAll()
        for i in stride(from: n - 1, through: 0, by: -1) {
            while !st.isEmpty && score[st.last!] <= score[i] { st.removeLast() }
            right[i] = st.isEmpty ? n : st.last!
            st.append(i)
        }
        var arr = (0..<n).map { (nums[$0], (i: $0 - left[$0]) * (right[$0] - $0)) }
        arr.sort { $0.0 > $1.0 }
        var ans = 1
        var remain = k
        for pair in arr {
            if remain <= 0 { break }
            let use = min(pair.1, remain)
            ans = ans * modPow(pair.0, use) % MOD
            remain -= use
        }
        return ans
    }

    private func primeScore(_ x0: Int, _ spf: [Int]) -> Int {
        var x = x0
        var seen = Set<Int>()
        while x > 1 {
            let p = spf[x]
            seen.insert(p)
            while x % p == 0 { x /= p }
        }
        return seen.count
    }

    private func modPow(_ a0: Int, _ b0: Int) -> Int {
        var a = a0 % MOD, b = b0, res = 1
        while b > 0 {
            if b & 1 != 0 { res = res * a % MOD }
            a = a * a % MOD
            b >>= 1
        }
        return res
    }
}
