// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

class Solution {
    func shiftingLetters(_ s: String, _ shifts: [Int]) -> String {
        var arr = Array(s)
        var total = 0
        let a = Int(Character("a").asciiValue!)
        for i in stride(from: arr.count - 1, through: 0, by: -1) {
            total = (total + shifts[i]) % 26
            let v = (Int(arr[i].asciiValue!) - a + total) % 26
            arr[i] = Character(UnicodeScalar(a + v)!)
        }
        return String(arr)
    }
}
