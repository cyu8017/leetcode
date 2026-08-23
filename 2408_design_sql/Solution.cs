// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

using System.Collections.Generic;

public class SQL {
    private readonly Dictionary<string, List<List<string>>> tables = new();
    private readonly Dictionary<string, int> nextID = new();

    public SQL(string[] names, int[] columns) {
        foreach (var name in names) {
            tables[name] = new List<List<string>>();
            nextID[name] = 1;
        }
    }

    public bool Ins(string name, IList<string> row) {
        if (!tables.ContainsKey(name)) return false;
        int id = nextID[name]++;
        var full = new List<string> { id.ToString() };
        full.AddRange(row);
        tables[name].Add(full);
        return true;
    }

    public void Rmv(string name, int rowId) {
        var rows = tables[name];
        for (int i = 0; i < rows.Count; i++) {
            if (int.Parse(rows[i][0]) == rowId) {
                rows.RemoveAt(i);
                return;
            }
        }
    }

    public string Sel(string name, int rowId, int columnId) {
        foreach (var r in tables[name]) {
            if (int.Parse(r[0]) == rowId) {
                if (columnId < 1 || columnId >= r.Count) return "<null>";
                return r[columnId];
            }
        }
        return "<null>";
    }

    public IList<string> Exp(string name) {
        var ans = new List<string>();
        foreach (var r in tables[name]) {
            string s = r[0];
            for (int j = 1; j < r.Count; j++) s += "," + r[j];
            ans.Add(s);
        }
        return ans;
    }
}
