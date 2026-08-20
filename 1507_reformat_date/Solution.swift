// LeetCode 1507 - Reformat Date
// https://leetcode.com/problems/reformat-date/

class Solution {
    func reformatDate(_ date: String) -> String {
        let months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        let parts = date.split(separator: " ").map(String.init)
        let day = Int(parts[0].dropLast(2))!
        let month = months.firstIndex(of: parts[1])! + 1
        return String(format: "%@-%02d-%02d", parts[2], month, day)
    }
}
