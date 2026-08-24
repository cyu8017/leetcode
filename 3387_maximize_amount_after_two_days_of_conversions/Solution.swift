// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

class Solution {
    func maxAmount(_ initialCurrency: String, _ pairs1: [[String]], _ rates1: [Double],
                   _ pairs2: [[String]], _ rates2: [Double]) -> Double {
        let amt1 = bellman(initialCurrency, pairs1, rates1)
        var ans = 1.0
        let g2 = buildRateGraph(pairs2, rates2)
        for (c, a) in amt1 where a > 0 {
            var dist = [c: a]
            var updated = true
            var it = 0
            while it < 100 && updated {
                updated = false
                it += 1
                for (from, tos) in g2 {
                    guard let df = dist[from], df != 0 else { continue }
                    for (to, rate) in tos {
                        let nv = df * rate
                        if dist[to] == nil || nv > dist[to]! {
                            dist[to] = nv
                            updated = true
                        }
                    }
                }
            }
            if let v = dist[initialCurrency], v > ans { ans = v }
        }
        return ans
    }

    private func buildRateGraph(_ pairs: [[String]], _ rates: [Double]) -> [String: [String: Double]] {
        var g = [String: [String: Double]]()
        for i in 0..<pairs.count {
            let a = pairs[i][0], b = pairs[i][1]
            g[a, default: [:]][b] = rates[i]
            g[b, default: [:]][a] = 1.0 / rates[i]
        }
        return g
    }

    private func bellman(_ start: String, _ pairs: [[String]], _ rates: [Double]) -> [String: Double] {
        let g = buildRateGraph(pairs, rates)
        var dist = [start: 1.0]
        for _ in 0..<100 {
            var updated = false
            for (from, tos) in g {
                guard let df = dist[from], df != 0 else { continue }
                for (to, rate) in tos {
                    let nv = df * rate
                    if dist[to] == nil || nv > dist[to]! {
                        dist[to] = nv
                        updated = true
                    }
                }
            }
            if !updated { break }
        }
        return dist
    }
}
