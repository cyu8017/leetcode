// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

class Solution {
    func garbageCollection(_ garbage: [String], _ travel: [Int]) -> Int {
        var ans = 0, lastM = 0, lastP = 0, lastG = 0
        for i in 0..<garbage.count {
            ans += garbage[i].count
            for c in garbage[i] {
                if c == "M" { lastM = i }
                else if c == "P" { lastP = i }
                else { lastG = i }
            }
        }
        var pref = [Int](repeating: 0, count: travel.count + 1)
        for i in 0..<travel.count { pref[i + 1] = pref[i] + travel[i] }
        return ans + pref[lastM] + pref[lastP] + pref[lastG]
    }
}
