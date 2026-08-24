// LeetCode 4009 - Minimum Possible Maximum Waiting Time
// https://leetcode.com/problems/minimum-possible-maximum-waiting-time/


class Solution {
    func minMaxWaitingTime(_ demand: [Int], _ fuel: [Int]) -> Int {
        let dem = demand
        let n = demand.count
        let f0 = fuel[0], f1 = fuel[1]
        if f0 < demand[0] && f1 < demand[0] { return -1 }
        func packKey(_ i: Int, _ f0: Int, _ f1: Int, _ d0: Int, _ d1: Int) -> Int {
            ((((i * 51 + f0) * 51 + f1) * 21 + d0) * 21 + d1)
        }
        var memo = [Int: Int]()
        func maxServe(_ i: Int, _ f0: Int, _ f1: Int, _ d0: Int, _ d1: Int) -> Int {
            if i == n { return i }
            let key = packKey(i, f0, f1, d0, d1)
            if let v = memo[key] { return v }
            let need = dem[i]
            let can0 = f0 >= need
            let can1 = f1 >= need
            var best = i
            if !can0 && !can1 {
                memo[key] = best
                return best
            }
            if can0 {
                let nd1 = d1 > d0 ? d1 - d0 : 0
                best = max(best, maxServe(i + 1, f0 - need, f1, need, nd1))
            }
            if can1 {
                let nd0 = d0 > d1 ? d0 - d1 : 0
                best = max(best, maxServe(i + 1, f0, f1 - need, nd0, need))
            }
            memo[key] = best
            return best
        }
        memo.removeAll()
        let bestServe = maxServe(0, f0, f1, 0, 0)
        if bestServe == 0 { return -1 }
        var W = 0
        func canWithW(_ i: Int, _ f0: Int, _ f1: Int, _ d0: Int, _ d1: Int) -> Bool {
            if i >= bestServe { return true }
            if i == n { return true }
            let key = packKey(i, f0, f1, d0, d1)
            if let v = memo[key] { return v == 2 }
            let need = dem[i]
            let can0 = f0 >= need
            let can1 = f1 >= need
            var ok = false
            if !can0 && !can1 {
                memo[key] = 1
                return false
            }
            if can0 && d0 <= W {
                let nd1 = d1 > d0 ? d1 - d0 : 0
                if canWithW(i + 1, f0 - need, f1, need, nd1) { ok = true }
            }
            if !ok && can1 && d1 <= W {
                let nd0 = d0 > d1 ? d0 - d1 : 0
                if canWithW(i + 1, f0, f1 - need, nd0, need) { ok = true }
            }
            memo[key] = ok ? 2 : 1
            return ok
        }
        var lo = 0, hi = 0
        for x in demand { hi += x }
        var ans = hi
        while lo <= hi {
            let mid = (lo + hi) / 2
            W = mid
            memo.removeAll()
            if canWithW(0, f0, f1, 0, 0) {
                ans = mid
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }
        return ans
    }
}
