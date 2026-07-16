// LeetCode 0481 - Magical String
// https://leetcode.com/problems/magical-string/

class Solution {
    func magicalString(_ n: Int) -> Int {
        if n == 0 {
            return 0
        }
        var seq = [1, 2, 2]
        var i = 2
        while seq.count < n {
            if seq[i] == 1 {
                seq.append(seq.last == 2 ? 1 : 2)
            } else {
                let nextVal = seq.last == 2 ? 1 : 2
                seq.append(contentsOf: [nextVal, nextVal])
            }
            i += 1
        }
        return seq.prefix(n).filter { $0 == 1 }.count
    }
}
