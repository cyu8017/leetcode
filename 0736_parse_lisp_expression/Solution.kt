// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

class Solution {
    private val tokens = ArrayList<String>()
    private var pos = 0

    fun evaluate(expression: String): Int {
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
        return parse(ArrayList<MutableMap<String, Int>>())
    }

    private fun parse(env: MutableList<MutableMap<String, Int>>): Int {
        val token = tokens[pos]
        if (token != "(") {
            pos++
            if (token[0].isDigit() || (token[0] == '-' && token.length > 1)) return token.toInt()
            for (i in env.size - 1 downTo 0) {
                if (env[i].containsKey(token)) return env[i][token]!!
            }
            return 0
        }
        pos++
        val op = tokens[pos++]
        if (op == "let") {
            env.add(HashMap())
            while (tokens[pos] != ")") {
                if (tokens[pos] == "(" || tokens[pos + 1] == ")") {
                    val value = parse(env)
                    pos++
                    env.removeAt(env.size - 1)
                    return value
                }
                val variable = tokens[pos++]
                env[env.size - 1][variable] = parse(env)
            }
        }
        if (op == "add") {
            val left = parse(env)
            val right = parse(env)
            pos++
            return left + right
        }
        if (op == "mult") {
            val left = parse(env)
            val right = parse(env)
            pos++
            return left * right
        }
        return 0
    }
}
