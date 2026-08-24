// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

class Solution {
    func distinctNames(_ ideas: [String]) -> Int {
        var groups = [Set<String>](repeating: [], count: 26)
        for idea in ideas {
            let arr = Array(idea)
            groups[Int(arr[0].asciiValue! - 97)].insert(String(arr.dropFirst()))
        }
        var ans = 0
        for i in 0..<26 {
            for j in (i + 1)..<26 {
                let overlap = groups[i].intersection(groups[j]).count
                ans += (groups[i].count - overlap) * (groups[j].count - overlap) * 2
            }
        }
        return ans
    }
}
