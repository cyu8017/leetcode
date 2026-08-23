// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string CountOfAtoms(string formula) {
        var st = new Stack<SortedDictionary<string, int>>();
        st.Push(new SortedDictionary<string, int>());
        int i = 0, n = formula.Length;
        while (i < n) {
            if (formula[i] == '(') { st.Push(new SortedDictionary<string, int>()); i++; }
            else if (formula[i] == ')') {
                i++;
                int start = i;
                while (i < n && char.IsDigit(formula[i])) i++;
                int mult = start < i ? int.Parse(formula.Substring(start, i - start)) : 1;
                var top = st.Pop();
                foreach (var kv in top) {
                    if (!st.Peek().ContainsKey(kv.Key)) st.Peek()[kv.Key] = 0;
                    st.Peek()[kv.Key] += kv.Value * mult;
                }
            } else {
                int start = i++;
                while (i < n && char.IsLower(formula[i])) i++;
                string atom = formula.Substring(start, i - start);
                start = i;
                while (i < n && char.IsDigit(formula[i])) i++;
                int count = start < i ? int.Parse(formula.Substring(start, i - start)) : 1;
                if (!st.Peek().ContainsKey(atom)) st.Peek()[atom] = 0;
                st.Peek()[atom] += count;
            }
        }
        var result = new StringBuilder();
        foreach (var kv in st.Peek()) {
            result.Append(kv.Key);
            if (kv.Value > 1) result.Append(kv.Value);
        }
        return result.ToString();
    }
}
