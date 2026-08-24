// LeetCode 2381 - Shifting Letters II
// https://leetcode.com/problems/shifting-letters-ii/

class Solution {
    func shiftingLetters(_ s: String, _ shifts: [[Int]]) -> String {
        var arr = Array(s)
        let n = arr.count
        var diff = [Int](repeating: 0, count: n + 1)
        for sh in shifts {
            let d = sh[2] == 0 ? -1 : 1
            diff[sh[0]] += d
            diff[sh[1] + 1] -= d
        }
        var cur = 0
        for i in 0..<n {
            cur = (cur + diff[i]) % 26
            if cur < 0 { cur += 26 }
            let v = Int(arr[i].asciiValue! - 97)
            arr[i] = Character(UnicodeScalar((v + cur) % 26 + 97)!)
        }
        return String(arr)
    }
}
