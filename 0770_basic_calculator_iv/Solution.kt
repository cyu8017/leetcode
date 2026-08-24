// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

class Solution {
    private val values = HashMap<String, Int>()
    private val tokens = ArrayList<String>()
    private var pos = 0

    private class ListKey(val items: List<String>) {
        fun count(): Int = items.size
        override fun equals(other: Any?): Boolean {
            if (other !is ListKey) return false
            return items == other.items
        }
        override fun hashCode(): Int = items.hashCode()
    }

    fun basicCalculatorIV(expression: String, evalvars: Array<String>, evalints: IntArray): List<String> {
        values.clear()
        for (i in evalvars.indices) values[evalvars[i]] = evalints[i]
        tokens.clear()
        val cur = StringBuilder()
        for (ch in expression) {
            when {
                ch == '(' || ch == ')' -> {
                    if (cur.isNotEmpty()) {
                        tokens.add(cur.toString())
                        cur.setLength(0)
                    }
                    tokens.add(ch.toString())
                }
                ch.isWhitespace() -> {
                    if (cur.isNotEmpty()) {
                        tokens.add(cur.toString())
                        cur.setLength(0)
                    }
                }
                else -> cur.append(ch)
            }
        }
        if (cur.isNotEmpty()) tokens.add(cur.toString())
        pos = 0
        val poly = parseExpr()
        val keys = ArrayList(poly.entries)
        keys.sortWith { a, b ->
            if (a.key.count() != b.key.count()) b.key.count().compareTo(a.key.count())
            else compareLists(a.key.items, b.key.items)
        }
        val answer = ArrayList<String>()
        for (kv in keys) {
            if (kv.value == 0) continue
            if (kv.key.count() == 0) answer.add(kv.value.toString())
            else {
                val term = StringBuilder(kv.value.toString())
                for (variable in kv.key.items) {
                    term.append('*')
                    term.append(variable)
                }
                answer.add(term.toString())
            }
        }
        return answer
    }

    private fun compareLists(a: List<String>, b: List<String>): Int {
        val n = minOf(a.size, b.size)
        for (i in 0 until n) {
            val cmp = a[i].compareTo(b[i])
            if (cmp != 0) return cmp
        }
        return a.size.compareTo(b.size)
    }

    private fun parseExpr(): MutableMap<ListKey, Int> {
        var poly = parseTerm()
        while (pos < tokens.size && (tokens[pos] == "+" || tokens[pos] == "-")) {
            val op = tokens[pos++]
            val right = parseTerm()
            poly = add(poly, if (op == "+") right else negate(right))
        }
        return poly
    }

    private fun parseTerm(): MutableMap<ListKey, Int> {
        var poly = parseFactor()
        while (pos < tokens.size && tokens[pos] == "*") {
            pos++
            poly = mul(poly, parseFactor())
        }
        return poly
    }

    private fun parseFactor(): MutableMap<ListKey, Int> {
        if (tokens[pos] == "(") {
            pos++
            val poly = parseExpr()
            pos++
            return poly
        }
        return atom(tokens[pos++])
    }

    private fun atom(token: String): MutableMap<ListKey, Int> {
        val poly = HashMap<ListKey, Int>()
        if (token[0].isLetter()) {
            if (values.containsKey(token)) poly[ListKey(ArrayList<String>())] = values[token]!!
            else poly[ListKey(arrayListOf(token))] = 1
        } else {
            poly[ListKey(ArrayList<String>())] = token.toInt()
        }
        return clean(poly)
    }

    private fun add(left: MutableMap<ListKey, Int>, right: MutableMap<ListKey, Int>): MutableMap<ListKey, Int> {
        val result = HashMap(left)
        for ((key, value) in right) {
            result[key] = result.getOrDefault(key, 0) + value
        }
        return clean(result)
    }

    private fun negate(poly: MutableMap<ListKey, Int>): MutableMap<ListKey, Int> {
        val result = HashMap<ListKey, Int>()
        for ((key, value) in poly) result[key] = -value
        return result
    }

    private fun mul(left: MutableMap<ListKey, Int>, right: MutableMap<ListKey, Int>): MutableMap<ListKey, Int> {
        val result = HashMap<ListKey, Int>()
        for ((lk, lv) in left) {
            for ((rk, rv) in right) {
                val keyList = ArrayList(lk.items)
                keyList.addAll(rk.items)
                keyList.sort()
                val key = ListKey(keyList)
                result[key] = result.getOrDefault(key, 0) + lv * rv
            }
        }
        return clean(result)
    }

    private fun clean(poly: MutableMap<ListKey, Int>): MutableMap<ListKey, Int> {
        poly.entries.removeIf { it.value == 0 }
        return poly
    }
}
