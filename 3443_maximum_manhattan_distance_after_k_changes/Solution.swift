// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

class Solution {
    func maxDistance(_ s: String, _ k: Int) -> Int {
        var ans = 0, lat = 0, lon = 0
        for (i, c) in s.enumerated() {
            if c == "N" { lat += 1 }
            else if c == "S" { lat -= 1 }
            else if c == "E" { lon += 1 }
            else { lon -= 1 }
            let md = abs(lat) + abs(lon)
            let steps = i + 1
            var cur = md + 2 * k
            if cur > steps { cur = steps }
            if cur > ans { ans = cur }
        }
        return ans
    }
}
