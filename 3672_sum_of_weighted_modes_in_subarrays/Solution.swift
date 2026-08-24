// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

class Solution {
    var cnt = [Int: Int]()
    var pq = [(Int, Int)]()

    func getMode() -> Int {
        while true {
            pq.sort { $0.0 != $1.0 ? $0.0 > $1.0 : $0.1 < $1.1 }
            let top = pq[0]
            let freq = top.0, val = -top.1
            if cnt[val, default: 0] == freq { return freq * val }
            pq.removeFirst()
        }
    }

    func modeWeight(_ nums: [Int], _ k: Int) -> Int {
        cnt = [:]
        pq = []
        for i in 0..<k {
            let x = nums[i]
            cnt[x, default: 0] += 1
            pq.append((cnt[x]!, -x))
        }
        var ans = getMode()
        if nums.count > k {
            for i in k..<nums.count {
                let x = nums[i], y = nums[i - k]
                cnt[x, default: 0] += 1
                cnt[y, default: 0] -= 1
                pq.append((cnt[x]!, -x))
                pq.append((cnt[y]!, -y))
                ans += getMode()
            }
        }
        return ans
    }
}
