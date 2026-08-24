// LeetCode 3208 - Alternating Groups II
// https://leetcode.com/problems/alternating-groups-ii/

class Solution {
    func numberOfAlternatingGroups(_ colors: [Int], _ k: Int) -> Int {
        let n = colors.count
        var cnt = 0, ans = 0
        for i in 0..<(n * 2) {
            if i > 0 && colors[i % n] == colors[(i - 1) % n] { cnt = 1 }
            else { cnt += 1 }
            if i >= n && cnt >= k { ans += 1 }
        }
        return ans
    }
}
