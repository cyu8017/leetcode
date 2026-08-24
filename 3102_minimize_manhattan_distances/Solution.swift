// LeetCode 3102 - Minimize Manhattan Distances
// https://leetcode.com/problems/minimize-manhattan-distances/

class Solution {
    func minimumDistance(_ points: [[Int]]) -> Int {
        var st1: [Int: Int] = [:]
        var st2: [Int: Int] = [:]
        for p in points {
            st1[p[0] + p[1], default: 0] += 1
            st2[p[0] - p[1], default: 0] += 1
        }
        func extremes(_ st: [Int: Int]) -> (Int, Int, Int, Int) {
            var min1 = Int.max, min2 = Int.max
            var max1 = Int.min, max2 = Int.min
            for (k, v) in st where v > 0 {
                if k < min1 { min2 = min1; min1 = k }
                else if k < min2 { min2 = k }
                if k > max1 { max2 = max1; max1 = k }
                else if k > max2 { max2 = k }
            }
            return (min1, min2, max1, max2)
        }
        let e1 = extremes(st1)
        let e2 = extremes(st2)
        var ans = Int.max
        for p in points {
            let a = p[0] + p[1], b = p[0] - p[1]
            let mx1 = (a == e1.2 && st1[a] == 1) ? e1.3 : e1.2
            let mn1 = (a == e1.0 && st1[a] == 1) ? e1.1 : e1.0
            let mx2 = (b == e2.2 && st2[b] == 1) ? e2.3 : e2.2
            let mn2 = (b == e2.0 && st2[b] == 1) ? e2.1 : e2.0
            ans = min(ans, max(mx1 - mn1, mx2 - mn2))
        }
        return ans
    }
}
