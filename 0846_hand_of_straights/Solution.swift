// LeetCode 0846 - Hand of Straights
// https://leetcode.com/problems/hand-of-straights/

class Solution {
    func isNStraightHand(_ hand: [Int], _ groupSize: Int) -> Bool {
        if hand.count % groupSize != 0 { return false }
        var count = [Int: Int]()
        for x in hand { count[x, default: 0] += 1 }
        let keys = count.keys.sorted()
        for start in keys {
            let need = count[start] ?? 0
            if need == 0 { continue }
            for x in start..<(start + groupSize) {
                let c = count[x] ?? 0
                if c < need { return false }
                count[x] = c - need
            }
        }
        return true
    }
}
