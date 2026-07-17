// LeetCode 1733 - Minimum Number of People to Teach
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

class Solution {
    func minimumTeachings(_ n: Int, _ languages: [[Int]], _ friendships: [[Int]]) -> Int {
        let users = languages.count
        var knows = [[Bool]](repeating: [Bool](repeating: false, count: n + 1), count: users)
        for user in 0..<users {
            for lang in languages[user] {
                knows[user][lang] = true
            }
        }
        var need = Set<Int>()
        for friendship in friendships {
            let u = friendship[0] - 1
            let v = friendship[1] - 1
            let shares = languages[u].contains { lang in knows[v][lang] }
            if !shares {
                need.insert(u)
                need.insert(v)
            }
        }
        if need.isEmpty {
            return 0
        }
        var best = Int.max
        for lang in 1...n {
            let teach = need.filter { user in !knows[user][lang] }.count
            best = min(best, teach)
        }
        return best
    }
}
