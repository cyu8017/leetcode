// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

class Solution {
    fun subdomainVisits(cpdomains: Array<String>): MutableList<String> {
        var counts = HashMap<String, Int>()
        for (item in cpdomains) {
            var space = item.indexOf(' ')
            var count = item.substring(0, space.toInt())
            var domain = item.substring(space + 1)
            while (true) {
                counts.merge(domain, count, Integer::sum)
                var dot = domain.indexOf('.')
                if (dot < 0) break
                domain = domain.substring(dot + 1)
            }
        }
        var ans = ArrayList<String>()
        for (Map.Entry<String, Integer> e : counts.entrySet()) {
            ans.add(e.getValue() + " " + e.getKey())
        }
        return ans
    }
}
