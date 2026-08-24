// LeetCode 3894 - Traffic Signal Color
// https://leetcode.com/problems/traffic-signal-color/

class Solution {
    func trafficSignal(_ timer: Int) -> String {
        if timer == 0 { return "Green" }
        if timer == 30 { return "Orange" }
        if timer > 30 && timer <= 90 { return "Red" }
        return "Invalid"
    }
}
