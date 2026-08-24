// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

class Solution {
    class SparseTableRMQ {
        var n = 0, maxLog = 0
        var fMax = [[Int]]()
        var fMin = [[Int]]()
        var lg = [Int]()

        init(_ data: [Int]) {
            n = data.count
            maxLog = 0
            while (1 << maxLog) <= n { maxLog += 1 }
            maxLog += 1
            fMax = Array(repeating: Array(repeating: 0, count: maxLog), count: n)
            fMin = Array(repeating: Array(repeating: 0, count: maxLog), count: n)
            lg = Array(repeating: 0, count: n + 1)
            if n >= 2 {
                for i in 2...n { lg[i] = lg[i >> 1] + 1 }
            }
            for i in 0..<n {
                fMax[i][0] = data[i]
                fMin[i][0] = data[i]
            }
            if maxLog > 1 {
                for j in 1..<maxLog {
                    let span = 1 << j
                    if n >= span {
                        for i in 0...(n - span) {
                            fMax[i][j] = max(fMax[i][j - 1], fMax[i + (1 << (j - 1))][j - 1])
                            fMin[i][j] = min(fMin[i][j - 1], fMin[i + (1 << (j - 1))][j - 1])
                        }
                    }
                }
            }
        }

        func queryMax(_ l: Int, _ r: Int) -> Int {
            let k = lg[r - l + 1]
            return max(fMax[l][k], fMax[r - (1 << k) + 1][k])
        }

        func queryMin(_ l: Int, _ r: Int) -> Int {
            let k = lg[r - l + 1]
            return min(fMin[l][k], fMin[r - (1 << k) + 1][k])
        }
    }

    func maxTotalValue(_ nums: [Int], _ k: Int) -> Int {
        let n = nums.count
        let st = SparseTableRMQ(nums)
        var pq = [(Int, Int, Int)]()
        for l in 0..<n {
            let val = st.queryMax(l, n - 1) - st.queryMin(l, n - 1)
            pq.append((val, l, n - 1))
        }
        var ans = 0
        for _ in 0..<k {
            pq.sort { $0.0 > $1.0 }
            let top = pq.removeFirst()
            ans += top.0
            let l = top.1, r = top.2
            if r > l {
                let nextVal = st.queryMax(l, r - 1) - st.queryMin(l, r - 1)
                pq.append((nextVal, l, r - 1))
            }
        }
        return ans
    }
}
