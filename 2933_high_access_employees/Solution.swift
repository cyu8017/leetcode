// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

class Solution {
    func findHighAccessEmployees(_ accessTimes: [[String]]) -> [String] {
        var m: [String: [Int]] = [:]
        for a in accessTimes {
            let name = a[0], t = Array(a[1])
            let hh = Int(String(t[0]))! * 10 + Int(String(t[1]))!
            let mm = Int(String(t[2]))! * 10 + Int(String(t[3]))!
            m[name, default: []].append(hh * 60 + mm)
        }
        var ans: [String] = []
        for (name, times0) in m {
            let times = times0.sorted()
            var i = 0
            while i + 2 < times.count {
                if times[i + 2] - times[i] < 60 {
                    ans.append(name)
                    break
                }
                i += 1
            }
        }
        return ans.sorted()
    }
}
