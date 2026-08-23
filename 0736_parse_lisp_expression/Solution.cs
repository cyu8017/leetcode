// LeetCode 0736 - Parse Lisp Expression
// https://leetcode.com/problems/parse-lisp-expression/

using System.Collections.Generic;

public class Solution {
    private List<string> tokens = new List<string>();
    private int pos;

    public int Evaluate(string expression) {
        tokens.Clear();
        var cur = new System.Text.StringBuilder();
        foreach (char ch in expression) {
            if (ch == '(' || ch == ')') {
                if (cur.Length > 0) { tokens.Add(cur.ToString()); cur.Clear(); }
                tokens.Add(ch.ToString());
            } else if (char.IsWhiteSpace(ch)) {
                if (cur.Length > 0) { tokens.Add(cur.ToString()); cur.Clear(); }
            } else cur.Append(ch);
        }
        if (cur.Length > 0) tokens.Add(cur.ToString());
        pos = 0;
        return Parse(new List<Dictionary<string, int>>());
    }

    private int Parse(List<Dictionary<string, int>> env) {
        string token = tokens[pos];
        if (token != "(") {
            pos++;
            if (char.IsDigit(token[0]) || (token[0] == '-' && token.Length > 1)) return int.Parse(token);
            for (int i = env.Count - 1; i >= 0; i--) {
                if (env[i].TryGetValue(token, out int v)) return v;
            }
            return 0;
        }
        pos++;
        string op = tokens[pos++];
        if (op == "let") {
            env.Add(new Dictionary<string, int>());
            while (tokens[pos] != ")") {
                if (tokens[pos] == "(" || tokens[pos + 1] == ")") {
                    int value = Parse(env);
                    pos++;
                    env.RemoveAt(env.Count - 1);
                    return value;
                }
                string var = tokens[pos++];
                env[env.Count - 1][var] = Parse(env);
            }
        }
        if (op == "add") {
            int left = Parse(env), right = Parse(env);
            pos++;
            return left + right;
        }
        if (op == "mult") {
            int left = Parse(env), right = Parse(env);
            pos++;
            return left * right;
        }
        return 0;
    }
}
