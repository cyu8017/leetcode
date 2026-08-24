// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution {
    func minimumRecolors(_ blocks: String, _ k: Int) -> Int {
        let s = Array(blocks)
        var white = 0
        for i in 0..<k where s[i] == "W" { white += 1 }
        var ans = white
        if s.count > k {
            for i in k..<s.count {
                if s[i] == "W" { white += 1 }
                if s[i - k] == "W" { white -= 1 }
                ans = min(ans, white)
            }
        }
        return ans
    }
}
