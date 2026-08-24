// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/


class Solution {
    fun findHighAccessEmployees(accessTimes: List<List<String>>): List<String> {
        val m = HashMap<String, MutableList<Int>>()
        for (a in accessTimes) {
            val name = a[0]
            val t = a[1]
            val hh = (t[0] - '0') * 10 + (t[1] - '0')
            val mm = (t[2] - '0') * 10 + (t[3] - '0')
            m.getOrPut(name) { ArrayList() }.add(hh * 60 + mm)
        }
        val ans = ArrayList<String>()
        for ((name, times) in m) {
            times.sort()
            for (i in 0..times.size - 3) {
                if (times[i + 2] - times[i] < 60) {
                    ans.add(name)
                    break
                }
            }
        }
        ans.sort()
        return ans
    }
}
