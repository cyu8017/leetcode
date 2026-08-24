// LeetCode 3206 - Alternating Groups I
// https://leetcode.com/problems/alternating-groups-i/

class Solution {
    func numberOfAlternatingGroups(_ colors: [Int]) -> Int {
        let k = 3, n = colors.count
        var cnt = 0, ans = 0
        for i in 0..<(n * 2) {
            if i > 0 && colors[i % n] == colors[(i - 1) % n] { cnt = 1 }
            else { cnt += 1 }
            if i >= n && cnt >= k { ans += 1 }
        }
        return ans
    }
}
