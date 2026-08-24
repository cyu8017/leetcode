// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

class Solution {
    func countDays(_ days: Int, _ meetings: [[Int]]) -> Int {
        let ms = meetings.sorted { $0[0] < $1[0] }
        var last = 0, ans = 0
        for e in ms {
            if last < e[0] { ans += e[0] - last - 1 }
            last = max(last, e[1])
        }
        ans += days - last
        return ans
    }
}
