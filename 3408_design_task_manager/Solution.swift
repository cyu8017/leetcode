// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

private struct TaskHeap {
    private var a: [(Int, Int, Int)] = [] // pri, taskId, userId
    var isEmpty: Bool { a.isEmpty }
    mutating func push(_ x: (Int, Int, Int)) {
        a.append(x)
        var i = a.count - 1
        while i > 0 {
            let p = (i - 1) / 2
            if better(a[p], a[i]) { break }
            a.swapAt(p, i)
            i = p
        }
    }
    mutating func pop() -> (Int, Int, Int) {
        let r = a[0]
        let last = a.removeLast()
        if !a.isEmpty {
            a[0] = last
            var i = 0
            while true {
                var s = i
                let l = 2 * i + 1, rg = 2 * i + 2
                if l < a.count && better(a[l], a[s]) { s = l }
                if rg < a.count && better(a[rg], a[s]) { s = rg }
                if s == i { break }
                a.swapAt(i, s)
                i = s
            }
        }
        return r
    }
    private func better(_ a: (Int, Int, Int), _ b: (Int, Int, Int)) -> Bool {
        if a.0 != b.0 { return a.0 > b.0 }
        return a.1 > b.1
    }
}

class TaskManager {
    private var h = TaskHeap()
    private var pri = [Int: Int]()
    private var user = [Int: Int]()

    init(_ tasks: [[Int]]) {
        for t in tasks { add(t[0], t[1], t[2]) }
    }

    func add(_ userId: Int, _ taskId: Int, _ priority: Int) {
        pri[taskId] = priority
        user[taskId] = userId
        h.push((priority, taskId, userId))
    }

    func edit(_ taskId: Int, _ newPriority: Int) {
        pri[taskId] = newPriority
        h.push((newPriority, taskId, user[taskId]!))
    }

    func rmv(_ taskId: Int) {
        pri.removeValue(forKey: taskId)
        user.removeValue(forKey: taskId)
    }

    func execTop() -> Int {
        while !h.isEmpty {
            let top = h.pop()
            if let p = pri[top.1], p == top.0, user[top.1] == top.2 {
                pri.removeValue(forKey: top.1)
                let uid = user.removeValue(forKey: top.1)!
                return uid
            }
        }
        return -1
    }
}
