// LeetCode 3964 - Minimum Lights to Illuminate a Road
// https://leetcode.com/problems/minimum-lights-to-illuminate-a-road/


class Solution {
    func minLights(_ lights: [Int]) -> Int {
        let n = lights.count
        var d = Array(repeating: 0, count: n)
        for i in 0..<n {
            let v = lights[i]
            if v > 0 {
                let l = max(0, i - v)
                let r = min(n - 1, i + v)
                d[l] += 1
                if r + 1 < n { d[r + 1] -= 1 }
            }
        }
        var s = 0, cnt = 0, ans = 0
        for x in d {
            s += x
            if s == 0 { cnt += 1 }
            else {
                ans += (cnt + 2) / 3
                cnt = 0
            }
        }
        ans += (cnt + 2) / 3
        return ans
    }
}
