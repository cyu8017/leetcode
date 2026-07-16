// LeetCode 0455 - Assign Cookies
// https://leetcode.com/problems/assign-cookies/

class Solution {
    func findContentChildren(_ g: [Int], _ s: [Int]) -> Int {
        let children = g.sorted()
        let cookies = s.sorted()
        var child = 0
        var cookie = 0

        while child < children.count && cookie < cookies.count {
            if cookies[cookie] >= children[child] {
                child += 1
            }
            cookie += 1
        }

        return child
    }
}
