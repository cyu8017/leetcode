// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

class Solution {
    private val parent = HashMap<String, String>()

    private fun find(x: String): String {
        var x = x
        parent.putIfAbsent(x, x)
        while (parent[x] != x) {
            parent[x] = parent[parent[x]!!]!!
            x = parent[x]!!
        }
        return x
    }

    private fun unite(a: String, b: String) {
        parent[find(a)] = find(b)
    }

    fun accountsMerge(accounts: List<List<String>>): List<List<String>> {
        val emailName = HashMap<String, String>()
        parent.clear()
        for (account in accounts) {
            val name = account[0]
            val first = account[1]
            for (i in 1 until account.size) {
                val email = account[i]
                parent.putIfAbsent(email, email)
                emailName[email] = name
                unite(first, email)
            }
        }
        val groups = HashMap<String, MutableList<String>>()
        for (email in parent.keys) {
            val root = find(email)
            groups.getOrPut(root) { ArrayList<String>() }.add(email)
        }
        val result = ArrayList<List<String>>()
        for (emails in groups.values) {
            emails.sort()
            val row = ArrayList<String>()
            row.add(emailName[emails[0]]!!)
            row.addAll(emails)
            result.add(row)
        }
        return result
    }
}
