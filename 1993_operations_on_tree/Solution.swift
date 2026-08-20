// LeetCode 1993 - Operations on Tree
// https://leetcode.com/problems/operations-on-tree/

class LockingTree {
    private var locked: [Int]
    private var parent: [Int]
    private var children: [[Int]]

    init(_ parent: [Int]) {
        let n = parent.count
        self.locked = Array(repeating: -1, count: n)
        self.parent = parent
        self.children = Array(repeating: [Int](), count: n)
        for son in 1..<n {
            children[parent[son]].append(son)
        }
    }

    func lock(_ num: Int, _ user: Int) -> Bool {
        if locked[num] == -1 {
            locked[num] = user
            return true
        }
        return false
    }

    func unlock(_ num: Int, _ user: Int) -> Bool {
        if locked[num] == user {
            locked[num] = -1
            return true
        }
        return false
    }

    func upgrade(_ num: Int, _ user: Int) -> Bool {
        var x = num
        while x != -1 {
            if locked[x] != -1 { return false }
            x = parent[x]
        }
        var find = false
        func dfs(_ u: Int) {
            for v in children[u] {
                if locked[v] != -1 {
                    locked[v] = -1
                    find = true
                }
                dfs(v)
            }
        }
        dfs(num)
        if !find { return false }
        locked[num] = user
        return true
    }
}
