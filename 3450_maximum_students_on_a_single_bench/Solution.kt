// LeetCode 3450 - Maximum Students on a Single Bench
// https://leetcode.com/problems/maximum-students-on-a-single-bench/

class Solution {
    fun maxStudentsOnBench(students: Array<IntArray>): Int {
        var bench = HashMap<Int, MutableSet<Int>>()
        for (s in students) {
            bench.getOrPut(s[1]) { HashSet() }.add(s[0])
        }
        var ans = 0
        for (set in bench.values) {
            if (set.size > ans) ans = set.size
        }
        return ans
    }
}
