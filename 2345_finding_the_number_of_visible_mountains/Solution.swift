// LeetCode 2345 - Finding the Number of Visible Mountains
// https://leetcode.com/problems/finding-the-number-of-visible-mountains/

class Solution {
    func visibleMountains(_ peaks: [[Int]]) -> Int {
        var arr = peaks.map { [$0[0] - $0[1], $0[0] + $0[1]] }
        arr.sort {
            if $0[0] == $1[0] { return $0[1] > $1[1] }
            return $0[0] < $1[0]
        }
        var ans = 0
        var maxR = Int.min
        var i = 0
        while i < arr.count {
            var j = i
            while j < arr.count && arr[j][0] == arr[i][0] && arr[j][1] == arr[i][1] { j += 1 }
            if arr[i][1] > maxR {
                if j - i == 1 { ans += 1 }
                maxR = arr[i][1]
            }
            i = j
        }
        return ans
    }
}
