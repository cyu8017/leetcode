// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

using System.Collections.Generic;

public class Solution {
    class Node {
        public Dictionary<int, Node> Children = new Dictionary<int, Node>();
        public int Cnt = 0;
    }

    public long CountPrefixSuffixPairs(string[] words) {
        var trie = new Node();
        long ans = 0;
        foreach (var s in words) {
            var node = trie;
            int m = s.Length;
            for (int i = 0; i < m; i++) {
                int p = s[i] * 32 + s[m - i - 1];
                if (!node.Children.TryGetValue(p, out var next)) {
                    next = new Node();
                    node.Children[p] = next;
                }
                node = next;
                ans += node.Cnt;
            }
            node.Cnt++;
        }
        return ans;
    }
}
