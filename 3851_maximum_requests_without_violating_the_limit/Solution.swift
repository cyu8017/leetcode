// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

class Solution {
    func maxRequests(_ requests: [[Int]], _ k: Int, _ window: Int) -> Int {
        var g = [Int: [Int]]()
        for r in requests {
            g[r[0], default: []].append(r[1])
        }
        var ans = requests.count
        for var ts in g.values {
            ts.sort()
            var kept = [Int]()
            for t in ts {
                while !kept.isEmpty && t - kept[0] > window { kept.removeFirst() }
                if kept.count < k { kept.append(t) }
                else { ans -= 1 }
            }
        }
        return ans
    }
}
