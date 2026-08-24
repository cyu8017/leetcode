// LeetCode 0649 - Dota2 Senate
// https://leetcode.com/problems/dota2-senate/

class Solution {
    func predictPartyVictory(_ senate: String) -> String {
        var radiant = [Int]()
        var dire = [Int]()
        let n = senate.count
        for (i, ch) in senate.enumerated() {
            if ch == "R" { radiant.append(i) } else { dire.append(i) }
        }
        var ri = 0, di = 0
        while ri < radiant.count && di < dire.count {
            let r = radiant[ri]
            let d = dire[di]
            ri += 1
            di += 1
            if r < d { radiant.append(r + n) } else { dire.append(d + n) }
        }
        return ri >= radiant.count ? "Dire" : "Radiant"
    }
}
