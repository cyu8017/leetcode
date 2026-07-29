// LeetCode 1058 - Minimize Rounding Error to Meet Target
// https://leetcode.com/problems/minimize-rounding-error-to-meet-target/

class Solution {
    func minimizeError(_ prices: [String], _ target: Int) -> String {
        var floors = 0
        var fracs: [Double] = []
        for p in prices {
            let value = Double(p)!
            let floor = Int(value)
            floors += floor
            let frac = value - Double(floor)
            if frac > 1e-9 {
                fracs.append(frac)
            }
        }
        let ceilCount = target - floors
        if ceilCount < 0 || ceilCount > fracs.count {
            return "-1"
        }
        fracs.sort(by: >)
        var error = 0.0
        for i in 0..<fracs.count {
            if i < ceilCount {
                error += 1 - fracs[i]
            } else {
                error += fracs[i]
            }
        }
        return String(format: "%.3f", error)
    }
}
