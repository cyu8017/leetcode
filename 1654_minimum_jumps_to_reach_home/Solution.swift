// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

class Solution {
    func minimumJumps(_ forbidden: [Int], _ a: Int, _ b: Int, _ x: Int) -> Int {
        let bad = Set(forbidden)
        let limit = max(x, forbidden.max() ?? 0) + a + b
        var q = [(0, 0, false)]
        var seen = Set(["0,0"])
        var head = 0
        while head < q.count {
            let (p, d, back) = q[head]
            head += 1
            if p == x { return d }
            for (np, nb) in [(p + a, false), (p - b, true)] {
                let key = "\(np),\(nb ? 1 : 0)"
                if np >= 0 && np <= limit && !bad.contains(np) && !seen.contains(key) && !(back && nb) {
                    seen.insert(key)
                    q.append((np, d + 1, nb))
                }
            }
        }
        return -1
    }
}
