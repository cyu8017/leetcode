// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

object Solution {
  def parseBoolExpr(expression: String): Boolean = {
    val stack = scala.collection.mutable.Stack.empty[Char]
    for (ch <- expression) {
      if (ch == ')') {
        val values = scala.collection.mutable.ListBuffer.empty[Boolean]
        while (stack.nonEmpty && !"&|!".contains(stack.top)) {
          val token = stack.pop()
          if (token == 't' || token == 'f') values += (token == 't')
        }
        val op = stack.pop()
        val result =
          if (op == '!') !values.head
          else if (op == '&') values.forall(identity)
          else values.exists(identity)
        stack.push(if (result) 't' else 'f')
      } else if (ch != ',') {
        stack.push(ch)
      }
    }
    stack.top == 't'
  }
}
