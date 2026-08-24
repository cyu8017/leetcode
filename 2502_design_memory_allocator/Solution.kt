// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

class Allocator(n: Int) {
    private val mem = IntArray(n)

    fun allocate(size: Int, mID: Int): Int {
        var freeCnt = 0
        for (i in mem.indices) {
            if (mem[i] == 0) {
                freeCnt++
                if (freeCnt == size) {
                    val start = i - size + 1
                    for (j in start..i) mem[j] = mID
                    return start
                }
            } else {
                freeCnt = 0
            }
        }
        return -1
    }

    fun freeMemory(mID: Int): Int {
        var cnt = 0
        for (i in mem.indices) {
            if (mem[i] == mID) {
                mem[i] = 0
                cnt++
            }
        }
        return cnt
    }
}
