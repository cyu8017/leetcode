// LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

class Solution {
    func maxTotalFruits(_ fruits: [[Int]], _ startPos: Int, _ k: Int) -> Int {
        let n = fruits.count
        var pref = [Int](repeating: 0, count: n + 1)
        var pos = [Int](repeating: 0, count: n)
        for i in 0..<n {
            pos[i] = fruits[i][0]
            pref[i + 1] = pref[i] + fruits[i][1]
        }
        func minSteps(_ left: Int, _ right: Int) -> Int {
            if right <= startPos { return startPos - left }
            if left >= startPos { return right - startPos }
            return min((startPos - left) + (right - left), (right - startPos) + (right - left))
        }
        var ans = 0, j = 0
        for i in 0..<n {
            while j < n && minSteps(pos[i], pos[j]) > k { j += 1 }
            if j <= i { ans = max(ans, pref[i + 1] - pref[j]) }
        }
        j = 0
        for i in 0..<n {
            while j <= i && minSteps(pos[j], pos[i]) > k { j += 1 }
            ans = max(ans, pref[i + 1] - pref[j])
        }
        return ans
    }
}
