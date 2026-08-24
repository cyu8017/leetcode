// LeetCode 0825 - Friends Of Appropriate Ages
// https://leetcode.com/problems/friends-of-appropriate-ages/

class Solution {
    func numFriendRequests(_ ages: [Int]) -> Int {
        var count = Array(repeating: 0, count: 121)
        for age in ages { count[age] += 1 }
        var ans = 0
        for x in 1...120 {
            if count[x] == 0 { continue }
            for y in 1...120 {
                if count[y] == 0 { continue }
                if Double(y) <= 0.5 * Double(x) + 7 || y > x || (y > 100 && x < 100) { continue }
                ans += count[x] * count[y]
                if x == y { ans -= count[x] }
            }
        }
        return ans
    }
}
