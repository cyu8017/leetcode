// LeetCode 1980 - Find Unique Binary String
// https://leetcode.com/problems/find-unique-binary-string/

class Solution {
    func findDifferentBinaryString(_ nums: [String]) -> String {
        let s = Set(nums)
        let n = nums.count
        let preferred = ["11", "101", "00", "10", "01", "000", "001", "010", "011", "100", "110", "111"]
        for cand in preferred where cand.count == n && !s.contains(cand) {
            return cand
        }
        for i in 0..<(1 << n) {
            var cand = ""
            for b in stride(from: n - 1, through: 0, by: -1) {
                cand.append((i >> b) & 1 == 1 ? "1" : "0")
            }
            if !s.contains(cand) { return cand }
        }
        return String(repeating: "0", count: n)
    }
}
