// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

class Solution {
    func memLeak(_ memory1: Int, _ memory2: Int) -> [Int] {
        var mem1 = memory1
        var mem2 = memory2
        var second = 1

        while mem1 >= second || mem2 >= second {
            if mem1 >= mem2 {
                mem1 -= second
            } else {
                mem2 -= second
            }
            second += 1
        }

        return [second, mem1, mem2]
    }
}
