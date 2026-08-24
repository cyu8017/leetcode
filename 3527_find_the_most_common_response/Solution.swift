// LeetCode 3527 - Find the Most Common Response
// https://leetcode.com/problems/find-the-most-common-response/

class Solution {
    func findCommonResponse(_ responses: [[String]]) -> String {
        var cnt = [String: Int]()
        for ws in responses {
            var s = Set<String>()
            for w in ws {
                if s.insert(w).inserted { cnt[w, default: 0] += 1 }
            }
        }
        var ans = responses[0][0]
        for (w, v) in cnt {
            if cnt[ans]! < v || (cnt[ans]! == v && w < ans) { ans = w }
        }
        return ans
    }
}
