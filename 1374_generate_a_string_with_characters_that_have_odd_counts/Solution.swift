// LeetCode 1374 - Generate a String With Characters That Have Odd Counts
// https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution {
    func generateTheString(_ n: Int) -> String {
        n % 2 != 0 ? String(repeating: "a", count: n) : String(repeating: "a", count: n - 1) + "b"
    }
}
