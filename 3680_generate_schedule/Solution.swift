// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

class Solution {
    var matches = [[Int]]()
    var used = [Bool]()
    var sched = [[Int]]()
    var last0 = -1, last1 = -1

    func dfs() -> Bool {
        if sched.count == matches.count { return true }
        for i in 0..<matches.count {
            if used[i] { continue }
            let m = matches[i]
            if m[0] == last0 || m[0] == last1 || m[1] == last0 || m[1] == last1 { continue }
            used[i] = true
            sched.append(m)
            let p0 = last0, p1 = last1
            last0 = m[0]; last1 = m[1]
            if dfs() { return true }
            last0 = p0; last1 = p1
            sched.removeLast()
            used[i] = false
        }
        return false
    }

    func generateSchedule(_ n: Int) -> [[Int]] {
        if n < 5 { return [] }
        matches = []
        for i in 0..<n {
            for j in 0..<n where i != j { matches.append([i, j]) }
        }
        used = Array(repeating: false, count: matches.count)
        sched = []
        last0 = -1; last1 = -1
        if dfs() { return sched }
        return []
    }
}
