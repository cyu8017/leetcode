// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

class Solution {
    func maxTaskAssign(_ tasks: [Int], _ workers: [Int], _ pills: Int, _ strength: Int) -> Int {
        let tasks = tasks.sorted()
        let workers = workers.sorted()
        var lo = 0, hi = min(tasks.count, workers.count)
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if can(tasks, workers, pills, strength, mid) { lo = mid }
            else { hi = mid - 1 }
        }
        return lo
    }

    private func can(_ tasks: [Int], _ workers: [Int], _ pills: Int, _ strength: Int, _ k: Int) -> Bool {
        if k == 0 { return true }
        var ws = Array(workers[(workers.count - k)...])
        var p = pills
        for i in stride(from: k - 1, through: 0, by: -1) {
            let task = tasks[i]
            if ws.last! >= task {
                ws.removeLast()
                continue
            }
            if p == 0 { return false }
            let need = task - strength
            var lo = 0, hi = ws.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if ws[mid] < need { lo = mid + 1 }
                else { hi = mid }
            }
            if lo == ws.count { return false }
            ws.remove(at: lo)
            p -= 1
        }
        return true
    }
}
