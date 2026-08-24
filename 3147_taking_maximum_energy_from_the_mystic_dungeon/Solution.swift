// LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon
// https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

class Solution {
    func maximumEnergy(_ energy: [Int], _ k: Int) -> Int {
        var ans = -(1 << 30)
        let n = energy.count
        for i in (n - k)..<n {
            var j = i, s = 0
            while j >= 0 {
                s += energy[j]
                ans = max(ans, s)
                j -= k
            }
        }
        return ans
    }
}
