// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution {
    func distributeCookies(_ cookies: [Int], _ k: Int) -> Int {
        var bags = [Int](repeating: 0, count: k)
        var ans = Int.max
        func dfs(_ i: Int) {
            if i == cookies.count {
                ans = min(ans, bags.max()!)
                return
            }
            var seen = Set<Int>()
            for j in 0..<bags.count {
                if !seen.insert(bags[j]).inserted { continue }
                bags[j] += cookies[i]
                if bags[j] < ans { dfs(i + 1) }
                bags[j] -= cookies[i]
                if bags[j] == 0 { break }
            }
        }
        dfs(0)
        return ans
    }
}
