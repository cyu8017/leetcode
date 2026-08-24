// LeetCode 3181 - Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

class Solution {
    func maxTotalReward(_ rewardValues: [Int]) -> Int {
        var a = rewardValues.sorted()
        var uniq: [Int] = []
        for v in a {
            if uniq.isEmpty || uniq.last != v { uniq.append(v) }
        }
        let maxBit = uniq.last! * 2
        let nwords = (maxBit + 64) / 64 + 1
        var f = Array(repeating: UInt64(0), count: nwords)
        f[0] = 1
        for v in uniq {
            let fullWords = v / 64
            let rem = v % 64
            var mask = Array(repeating: UInt64(0), count: nwords)
            for i in 0..<fullWords { mask[i] = f[i] }
            if rem > 0 && fullWords < nwords {
                mask[fullWords] = f[fullWords] & ((UInt64(1) << rem) - 1)
            }
            var shifted = Array(repeating: UInt64(0), count: nwords)
            if rem == 0 {
                for i in 0..<nwords {
                    let dest = i + fullWords
                    if dest < nwords { shifted[dest] = mask[i] }
                }
            } else {
                for i in 0..<nwords {
                    let dest = i + fullWords
                    if dest < nwords { shifted[dest] |= mask[i] << rem }
                    if dest + 1 < nwords { shifted[dest + 1] |= mask[i] >> (64 - rem) }
                }
            }
            for i in 0..<nwords { f[i] |= shifted[i] }
        }
        for i in stride(from: maxBit, through: 0, by: -1) {
            if (f[i / 64] >> (i % 64)) & 1 == 1 { return i }
        }
        return 0
    }
}
