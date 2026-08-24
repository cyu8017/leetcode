// LeetCode 0672 - Bulb Switcher II
// https://leetcode.com/problems/bulb-switcher-ii/

class Solution {
    func flipLights(_ n: Int, _ presses: Int) -> Int {
        let n = min(n, 3)
        if presses == 0 { return 1 }
        let onePress = [2, 3, 4]
        let twoPress = [2, 4, 7]
        let manyPress = [2, 4, 8]
        if presses == 1 { return onePress[n - 1] }
        if presses == 2 { return twoPress[n - 1] }
        return manyPress[n - 1]
    }
}
