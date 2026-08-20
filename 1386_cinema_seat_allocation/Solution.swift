// LeetCode 1386 - Cinema Seat Allocation
// https://leetcode.com/problems/cinema-seat-allocation/

class Solution {
    func maxNumberOfFamilies(_ n: Int, _ reservedSeats: [[Int]]) -> Int {
        var rows = [Int: Int]()
        for seat in reservedSeats {
            let r = seat[0], c = seat[1]
            if c >= 2 && c <= 9 { rows[r, default: 0] |= 1 << (c - 2) }
        }
        var ans = 2 * (n - rows.count)
        for m in rows.values {
            let left = m & 0b00001111 == 0
            let right = m & 0b11110000 == 0
            let middle = m & 0b00111100 == 0
            if left && right { ans += 2 }
            else if left || right || middle { ans += 1 }
        }
        return ans
    }
}
