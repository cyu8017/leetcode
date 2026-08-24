// LeetCode 2137 - Pour Water Between Buckets to Make Water Levels Equal
// https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/

class Solution {
    func equalizeWater(_ buckets: [Int], _ loss: Int) -> Double {
        var lo = 0.0, hi = Double(buckets.max() ?? 0)
        for _ in 0..<60 {
            let mid = (lo + hi) / 2
            var have = 0.0, need = 0.0
            for b in buckets {
                if Double(b) >= mid { have += Double(b) - mid }
                else { need += mid - Double(b) }
            }
            if have * (1.0 - Double(loss) / 100.0) >= need { lo = mid }
            else { hi = mid }
        }
        return lo
    }
}
