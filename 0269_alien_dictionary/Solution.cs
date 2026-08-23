// LeetCode 0269 - Alien Dictionary
// https://leetcode.com/problems/alien-dictionary/

using System.Collections.Generic;
using System.Linq;
using System.Text;

public class Solution {
    public string AlienOrder(string[] words) {
        var graph = new Dictionary<char, HashSet<char>>();
        var indegree = new Dictionary<char, int>();

        foreach (string word in words) {
            foreach (char ch in word) {
                if (!graph.ContainsKey(ch)) {
                    graph[ch] = new HashSet<char>();
                    indegree[ch] = 0;
                }
            }
        }

        for (int i = 0; i < words.Length - 1; i++) {
            string first = words[i];
            string second = words[i + 1];
            if (first.Length > second.Length && first.StartsWith(second)) {
                return "";
            }
            int limit = System.Math.Min(first.Length, second.Length);
            for (int j = 0; j < limit; j++) {
                char left = first[j];
                char right = second[j];
                if (left != right) {
                    if (!graph[left].Contains(right)) {
                        graph[left].Add(right);
                        indegree[right]++;
                    }
                    break;
                }
            }
        }

        var queue = new Queue<char>();
        foreach (var entry in indegree) {
            if (entry.Value == 0) {
                queue.Enqueue(entry.Key);
            }
        }

        var order = new StringBuilder();
        while (queue.Count > 0) {
            char ch = queue.Dequeue();
            order.Append(ch);
            foreach (char next in graph[ch]) {
                indegree[next]--;
                if (indegree[next] == 0) {
                    queue.Enqueue(next);
                }
            }
        }

        return order.Length == indegree.Count ? order.ToString() : "";
    }
}
