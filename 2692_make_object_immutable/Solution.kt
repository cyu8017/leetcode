// LeetCode 2692 - Make Object Immutable
// https://leetcode.com/problems/make-object-immutable/

class Solution {
    fun makeImmutable(obj: java.util.TreeMap<String, Int>): java.util.TreeMap<String, Int> =
        java.util.TreeMap(obj)
}
