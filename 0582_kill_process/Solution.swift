// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/

class Solution {
    func killProcess(_ pid: [Int], _ ppid: [Int], _ kill: Int) -> [Int] {
        var children = [Int: [Int]]()
        for i in 0..<pid.count {
            children[ppid[i], default: []].append(pid[i])
        }
        var result = [Int]()
        var queue = [kill]
        var idx = 0
        while idx < queue.count {
            let process = queue[idx]
            idx += 1
            result.append(process)
            if let kids = children[process] {
                queue.append(contentsOf: kids)
            }
        }
        return result
    }
}
