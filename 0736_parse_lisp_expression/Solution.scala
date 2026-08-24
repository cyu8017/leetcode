// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

object Solution {
  def evaluate(expression: String): Int = {
    val tokens = scala.collection.mutable.ArrayBuffer.empty[String]
    val cur = new StringBuilder
    for (ch <- expression) {
      if (ch == '(' || ch == ')') {
        if (cur.length > 0) {
          tokens += cur.toString
          cur.setLength(0)
        }
        tokens += ch.toString
      } else if (ch.isWhitespace) {
        if (cur.length > 0) {
          tokens += cur.toString
          cur.setLength(0)
        }
      } else cur.append(ch)
    }
    if (cur.length > 0) tokens += cur.toString
    var pos = 0
    def parse(env: scala.collection.mutable.ArrayBuffer[scala.collection.mutable.HashMap[String, Int]]): Int = {
      val token = tokens(pos)
      if (token != "(") {
        pos += 1
        if (token.charAt(0).isDigit || (token.charAt(0) == '-' && token.length > 1)) return token.toInt
        var i = env.length - 1
        while (i >= 0) {
          if (env(i).contains(token)) return env(i)(token)
          i -= 1
        }
        return 0
      }
      pos += 1
      val op = tokens(pos)
      pos += 1
      if (op == "let") {
        env += scala.collection.mutable.HashMap.empty[String, Int]
        while (tokens(pos) != ")") {
          if (tokens(pos) == "(" || tokens(pos + 1) == ")") {
            val value = parse(env)
            pos += 1
            env.remove(env.length - 1)
            return value
          }
          val variable = tokens(pos)
          pos += 1
          env.last(variable) = parse(env)
        }
      }
      if (op == "add") {
        val left = parse(env)
        val right = parse(env)
        pos += 1
        return left + right
      }
      if (op == "mult") {
        val left = parse(env)
        val right = parse(env)
        pos += 1
        return left * right
      }
      0
    }
    parse(scala.collection.mutable.ArrayBuffer.empty)
  }
}
