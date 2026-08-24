// LeetCode 2125 - Number of Laser Beams in a Bank
// https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution {
    func numberOfBeams(_ bank: [String]) -> Int {
        var ans = 0, prev = 0
        for row in bank {
            let cnt = row.filter { $0 == "1" }.count
            if cnt > 0 {
                ans += prev * cnt
                prev = cnt
            }
        }
        return ans
    }
}
