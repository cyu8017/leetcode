# LeetCode 0736 - Parse Lisp Expression
# https://leetcode.com/problems/parse-lisp-expression/


class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = expression.replace("(", " ( ").replace(")", " ) ").split()
        pos = 0

        def parse(env: list[dict[str, int]]) -> int:
            nonlocal pos
            token = tokens[pos]
            if token != "(":
                pos += 1
                if token.lstrip("-").isdigit():
                    return int(token)
                for scope in reversed(env):
                    if token in scope:
                        return scope[token]
                raise KeyError(token)

            pos += 1
            op = tokens[pos]
            pos += 1

            if op == "let":
                env.append({})
                while tokens[pos] != ")":
                    if tokens[pos] == "(" or tokens[pos + 1] == ")":
                        value = parse(env)
                        pos += 1
                        env.pop()
                        return value
                    var = tokens[pos]
                    pos += 1
                    env[-1][var] = parse(env)

            if op == "add":
                left = parse(env)
                right = parse(env)
                pos += 1
                return left + right

            if op == "mult":
                left = parse(env)
                right = parse(env)
                pos += 1
                return left * right

            raise ValueError(op)

        return parse([])
