// LeetCode 3395 - Subsequences with a Unique Middle Mode I
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

class Solution {
    func subsequencesWithMiddleMode(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = nums.count
        var ans = 0
        if n < 5 { return 0 }
        for mid in 2..<(n - 2) {
            for a in 0..<mid {
                for b in (a + 1)..<mid {
                    for c in (mid + 1)..<n {
                        for d in (c + 1)..<n {
                            let seq = [nums[a], nums[b], nums[mid], nums[c], nums[d]]
                            if uniqueMode(seq) { ans = (ans + 1) % mod }
                        }
                    }
                }
            }
        }
        return ans
    }

    private func uniqueMode(_ a: [Int]) -> Bool {
        var freq = [Int: Int]()
        for x in a { freq[x, default: 0] += 1 }
        var best = 0, cnt = 0
        for f in freq.values {
            if f > best { best = f; cnt = 1 }
            else if f == best { cnt += 1 }
        }
        return cnt == 1
    }
}
