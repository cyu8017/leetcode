// LeetCode 1096 - Brace Expansion II
// https://leetcode.com/problems/brace-expansion-ii/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> BraceExpansionII(string expression) {
        (HashSet<string> union, int next) Parse(string expr, int i) {
            var union = new HashSet<string>();
            var cur = new HashSet<string> { "" };
            while (i < expr.Length && expr[i] != '}') {
                if (expr[i] == '{') {
                    var (nested, ni) = Parse(expr, i + 1);
                    var next = new HashSet<string>();
                    foreach (string a in cur) {
                        foreach (string b in nested) {
                            next.Add(a + b);
                        }
                    }
                    cur = next;
                    i = ni;
                } else if (expr[i] == ',') {
                    union.UnionWith(cur);
                    cur = new HashSet<string> { "" };
                    i++;
                } else {
                    int j = i;
                    while (j < expr.Length && char.IsLetter(expr[j])) {
                        j++;
                    }
                    string token = expr.Substring(i, j - i);
                    var next = new HashSet<string>();
                    foreach (string a in cur) {
                        next.Add(a + token);
                    }
                    cur = next;
                    i = j;
                }
            }
            union.UnionWith(cur);
            return (union, i + 1);
        }

        var (result, _) = Parse(expression, 0);
        return result.OrderBy(x => x).ToList();
    }
}
