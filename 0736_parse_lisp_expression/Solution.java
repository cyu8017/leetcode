// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

import java.util.*;

class Solution {
    private List<String> tokens = new ArrayList<>();
    private int pos;

    public int evaluate(String expression) {
        tokens.clear();
        StringBuilder cur = new StringBuilder();
        for (char ch : expression.toCharArray()) {
            if (ch == '(' || ch == ')') {
                if (cur.length() > 0) { tokens.add(cur.toString()); cur.setLength(0); }
                tokens.add(String.valueOf(ch));
            } else if (Character.isWhitespace(ch)) {
                if (cur.length() > 0) { tokens.add(cur.toString()); cur.setLength(0); }
            } else cur.append(ch);
        }
        if (cur.length() > 0) tokens.add(cur.toString());
        pos = 0;
        return parse(new ArrayList<>());
    }

    private int parse(List<Map<String, Integer>> env) {
        String token = tokens.get(pos);
        if (!token.equals("(")) {
            pos++;
            if (Character.isDigit(token.charAt(0)) || (token.charAt(0) == '-' && token.length() > 1))
                return Integer.parseInt(token);
            for (int i = env.size() - 1; i >= 0; i--) {
                if (env.get(i).containsKey(token)) return env.get(i).get(token);
            }
            return 0;
        }
        pos++;
        String op = tokens.get(pos++);
        if (op.equals("let")) {
            env.add(new HashMap<>());
            while (!tokens.get(pos).equals(")")) {
                if (tokens.get(pos).equals("(") || tokens.get(pos + 1).equals(")")) {
                    int value = parse(env);
                    pos++;
                    env.remove(env.size() - 1);
                    return value;
                }
                String var = tokens.get(pos++);
                env.get(env.size() - 1).put(var, parse(env));
            }
        }
        if (op.equals("add")) {
            int left = parse(env), right = parse(env);
            pos++;
            return left + right;
        }
        if (op.equals("mult")) {
            int left = parse(env), right = parse(env);
            pos++;
            return left * right;
        }
        return 0;
    }
}
