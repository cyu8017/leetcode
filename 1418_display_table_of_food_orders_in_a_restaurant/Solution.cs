// LeetCode 1418 - Display Table Of Food Orders In A Restaurant
// https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

using System.Collections.Generic;
using System.Linq;
public class Solution {
    public IList<IList<string>> DisplayTable(IList<IList<string>> orders) {
        var foods = orders.Select(o => o[2]).Distinct().OrderBy(f => f, System.StringComparer.Ordinal).ToList();
        var tables = orders.Select(o => int.Parse(o[1])).Distinct().OrderBy(t => t).ToList();
        var counts = new Dictionary<(int, string), int>();
        foreach (var o in orders) {
            var key = (int.Parse(o[1]), o[2]);
            if (!counts.ContainsKey(key)) counts[key] = 0;
            counts[key]++;
        }
        var result = new List<IList<string>>();
        var header = new List<string> { "Table" }; header.AddRange(foods); result.Add(header);
        foreach (int table in tables) {
            var row = new List<string> { table.ToString() };
            foreach (string food in foods)
                row.Add(counts.ContainsKey((table, food)) ? counts[(table, food)].ToString() : "0");
            result.Add(row);
        }
        return result;
    }
}
