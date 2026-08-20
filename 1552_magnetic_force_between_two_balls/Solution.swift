// LeetCode 1552 - Magnetic Force Between Two Balls
// https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution {
    func maxDistance(_ position: [Int], _ m: Int) -> Int {
        let pos = position.sorted()
        var lo = 1, hi = (pos.last! - pos.first!) / (m - 1)
        while lo <= hi {
            let mid = (lo + hi) / 2
            var count = 1, last = pos[0]
            for x in pos.dropFirst() {
                if x - last >= mid {
                    count += 1
                    last = x
                }
            }
            if count >= m {
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return hi
    }
}
