// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

class Solution {
    func alertNames(_ keyName: [String], _ keyTime: [String]) -> [String] {
        var times = [String: [Int]]()
        for (name, t) in zip(keyName, keyTime) {
            let parts = t.split(separator: ":").map { Int($0)! }
            times[name, default: []].append(parts[0] * 60 + parts[1])
        }
        var ans = [String]()
        for (name, arr) in times {
            let a = arr.sorted()
            for i in 0..<(a.count - 2) {
                if a[i + 2] - a[i] <= 60 {
                    ans.append(name)
                    break
                }
            }
        }
        return ans.sorted()
    }
}
