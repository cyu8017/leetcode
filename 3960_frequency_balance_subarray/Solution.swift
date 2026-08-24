// LeetCode 3960 - Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/


class Solution {
    func getLength(_ nums: [Int]) -> Int {
        let n = nums.count
        var ans = 1
        for l in 0..<n {
            var cnt = [Int: Int]()
            var freq = [Int: Int]()
            for r in l..<n {
                let x = nums[r]
                let c = cnt[x, default: 0]
                if let fc0 = freq[c], fc0 > 0 {
                    let fc = fc0 - 1
                    if fc == 0 { freq.removeValue(forKey: c) }
                    else { freq[c] = fc }
                }
                cnt[x] = c + 1
                freq[cnt[x]!, default: 0] += 1
                let cx = cnt[x]!
                if cnt.count == 1 || (freq.count == 2 && (freq[cx * 2, default: 0] > 0 || (cx % 2 == 0 && freq[cx / 2, default: 0] > 0))) {
                    ans = max(ans, r - l + 1)
                }
            }
        }
        return ans
    }
}
