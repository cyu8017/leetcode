// LeetCode 0401 - Binary Watch
// https://leetcode.com/problems/binary-watch/

class Solution {
    func readBinaryWatch(_ turnedOn: Int) -> [String] {
        var result: [String] = []
        for hour in 0..<12 {
            for minute in 0..<60 {
                if bitCount(hour) + bitCount(minute) == turnedOn {
                    result.append(String(format: "%d:%02d", hour, minute))
                }
            }
        }
        return result
    }

    private func bitCount(_ value: Int) -> Int {
        var count = 0
        var n = value
        while n > 0 {
            count += n & 1
            n >>= 1
        }
        return count
    }
}
