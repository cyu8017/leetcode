// LeetCode 0770 - Basic Calculator IV
// https://leetcode.com/problems/basic-calculator-iv/

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution {
    private Dictionary<string, int> values = new Dictionary<string, int>();
    private List<string> tokens = new List<string>();
    private int pos;

    public IList<string> BasicCalculatorIV(string expression, string[] evalvars, int[] evalints) {
        values.Clear();
        for (int i = 0; i < evalvars.Length; i++) values[evalvars[i]] = evalints[i];
        tokens.Clear();
        var cur = new StringBuilder();
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
        var poly = ParseExpr();
        var keys = poly.ToList();
        keys.Sort((a, b) => {
            if (a.Key.Count != b.Key.Count) return b.Key.Count.CompareTo(a.Key.Count);
            return CompareLists(a.Key, b.Key);
        });
        var answer = new List<string>();
        foreach (var kv in keys) {
            if (kv.Value == 0) continue;
            if (kv.Key.Count == 0) answer.Add(kv.Value.ToString());
            else {
                var term = new StringBuilder(kv.Value.ToString());
                foreach (string var in kv.Key) { term.Append('*'); term.Append(var); }
                answer.Add(term.ToString());
            }
        }
        return answer;
    }

    private int CompareLists(List<string> a, List<string> b) {
        int n = Math.Min(a.Count, b.Count);
        for (int i = 0; i < n; i++) {
            int cmp = string.CompareOrdinal(a[i], b[i]);
            if (cmp != 0) return cmp;
        }
        return a.Count.CompareTo(b.Count);
    }

    private Dictionary<ListKey, int> ParseExpr() {
        var poly = ParseTerm();
        while (pos < tokens.Count && (tokens[pos] == "+" || tokens[pos] == "-")) {
            string op = tokens[pos++];
            var right = ParseTerm();
            poly = Add(poly, op == "+" ? right : Negate(right));
        }
        return poly;
    }

    private Dictionary<ListKey, int> ParseTerm() {
        var poly = ParseFactor();
        while (pos < tokens.Count && tokens[pos] == "*") {
            pos++;
            poly = Mul(poly, ParseFactor());
        }
        return poly;
    }

    private Dictionary<ListKey, int> ParseFactor() {
        if (tokens[pos] == "(") {
            pos++;
            var poly = ParseExpr();
            pos++;
            return poly;
        }
        return Atom(tokens[pos++]);
    }

    private Dictionary<ListKey, int> Atom(string token) {
        var poly = new Dictionary<ListKey, int>();
        if (char.IsLetter(token[0])) {
            if (values.TryGetValue(token, out int v)) poly[new ListKey(new List<string>())] = v;
            else poly[new ListKey(new List<string> { token })] = 1;
        } else poly[new ListKey(new List<string>())] = int.Parse(token);
        return Clean(poly);
    }

    private Dictionary<ListKey, int> Add(Dictionary<ListKey, int> left, Dictionary<ListKey, int> right) {
        var result = new Dictionary<ListKey, int>(left);
        foreach (var kv in right) {
            if (!result.ContainsKey(kv.Key)) result[kv.Key] = 0;
            result[kv.Key] += kv.Value;
        }
        return Clean(result);
    }

    private Dictionary<ListKey, int> Negate(Dictionary<ListKey, int> poly) {
        var result = new Dictionary<ListKey, int>();
        foreach (var kv in poly) result[kv.Key] = -kv.Value;
        return result;
    }

    private Dictionary<ListKey, int> Mul(Dictionary<ListKey, int> left, Dictionary<ListKey, int> right) {
        var result = new Dictionary<ListKey, int>();
        foreach (var lk in left) {
            foreach (var rk in right) {
                var keyList = new List<string>(lk.Key.Items);
                keyList.AddRange(rk.Key.Items);
                keyList.Sort(StringComparer.Ordinal);
                var key = new ListKey(keyList);
                if (!result.ContainsKey(key)) result[key] = 0;
                result[key] += lk.Value * rk.Value;
            }
        }
        return Clean(result);
    }

    private Dictionary<ListKey, int> Clean(Dictionary<ListKey, int> poly) {
        var zeros = poly.Where(kv => kv.Value == 0).Select(kv => kv.Key).ToList();
        foreach (var key in zeros) poly.Remove(key);
        return poly;
    }

    private sealed class ListKey : IEquatable<ListKey> {
        public List<string> Items { get; }
        public ListKey(List<string> items) { Items = items; }
        public int Count => Items.Count;
        public bool Equals(ListKey other) {
            if (other is null || Items.Count != other.Items.Count) return false;
            for (int i = 0; i < Items.Count; i++) if (Items[i] != other.Items[i]) return false;
            return true;
        }
        public override bool Equals(object obj) => Equals(obj as ListKey);
        public override int GetHashCode() {
            int h = 17;
            foreach (string s in Items) h = h * 31 + s.GetHashCode();
            return h;
        }
    }
}
