// LeetCode 1993
// https://leetcode.com/problems/operations-on-tree/

class LockingTree(parent: IntArray) {
    private val locked = IntArray(parent.size) { -1 }
    private val parentArr = parent
    private val children = Array(parent.size) { mutableListOf<Int>() }

    init {
        for (son in 1 until parent.size) children[parent[son]].add(son)
    }

    fun lock(num: Int, user: Int): Boolean {
        if (locked[num] == -1) {
            locked[num] = user
            return true
        }
        return false
    }

    fun unlock(num: Int, user: Int): Boolean {
        if (locked[num] == user) {
            locked[num] = -1
            return true
        }
        return false
    }

    fun upgrade(num: Int, user: Int): Boolean {
        var x = num
        while (x != -1) {
            if (locked[x] != -1) return false
            x = parentArr[x]
        }
        var find = false
        fun dfs(u: Int) {
            for (v in children[u]) {
                if (locked[v] != -1) {
                    locked[v] = -1
                    find = true
                }
                dfs(v)
            }
        }
        dfs(num)
        if (!find) return false
        locked[num] = user
        return true
    }
}
