// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

class Solution {
    func pushDominoes(_ dominoes: String) -> String {
        var arr = Array(dominoes)
        let n = arr.count
        var force = Array(repeating: 0, count: n)
        var f = 0
        for i in 0..<n {
            if arr[i] == "R" { f = n }
            else if arr[i] == "L" { f = 0 }
            else { f = max(f - 1, 0) }
            force[i] += f
        }
        f = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            if arr[i] == "L" { f = n }
            else if arr[i] == "R" { f = 0 }
            else { f = max(f - 1, 0) }
            force[i] -= f
        }
        for i in 0..<n {
            if force[i] > 0 { arr[i] = "R" }
            else if force[i] < 0 { arr[i] = "L" }
            else { arr[i] = "." }
        }
        return String(arr)
    }
}
