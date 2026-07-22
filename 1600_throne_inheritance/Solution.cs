// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

using System.Collections.Generic;

public class ThroneInheritance {
    private readonly string king;
    private readonly Dictionary<string, List<string>> children = new();
    private readonly HashSet<string> dead = new();

    public ThroneInheritance(string kingName) {
        king = kingName;
        children[kingName] = new List<string>();
    }

    public void Birth(string parentName, string childName) {
        if (!children.ContainsKey(parentName)) children[parentName] = new List<string>();
        children[parentName].Add(childName);
        if (!children.ContainsKey(childName)) children[childName] = new List<string>();
    }

    public void Death(string name) {
        dead.Add(name);
    }

    public IList<string> GetInheritanceOrder() {
        var order = new List<string>();
        Visit(king, order);
        return order;
    }

    private void Visit(string name, List<string> order) {
        if (!dead.Contains(name)) order.Add(name);
        if (!children.TryGetValue(name, out var kids)) return;
        foreach (var child in kids) Visit(child, order);
    }
}
