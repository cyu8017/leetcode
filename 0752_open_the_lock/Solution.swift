// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

class Solution {
    func openLock(_ deadends: [String], _ target: String) -> Int {
        let dead = Set(deadends)
        if dead.contains("0000") { return -1 }
        var queue = ["0000"]
        var seen = Set(["0000"])
        var idx = 0
        var steps = 0
        while idx < queue.count {
            let size = queue.count - idx
            for _ in 0..<size {
                let cur = queue[idx]
                idx += 1
                if cur == target { return steps }
                var chars = Array(cur)
                for i in 0..<4 {
                    let orig = chars[i]
                    let d = Int(String(orig))!
                    for delta in [-1, 1] {
                        chars[i] = Character(String((d + delta + 10) % 10))
                        let nxt = String(chars)
                        if !dead.contains(nxt) && seen.insert(nxt).inserted { queue.append(nxt) }
                    }
                    chars[i] = orig
                }
            }
            steps += 1
        }
        return -1
    }
}
