// LeetCode 3045 - Count Prefix and Suffix Pairs II
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/

import java.util.HashMap;
import java.util.Map;

class Solution {
    class Node {
        Map<Integer, Node> children = new HashMap<>();
        int cnt = 0;
    }

    public long countPrefixSuffixPairs(String[] words) {
        Node trie = new Node();
        long ans = 0;
        for (String s : words) {
            Node node = trie;
            int m = s.length();
            for (int i = 0; i < m; i++) {
                int p = s.charAt(i) * 32 + s.charAt(m - i - 1);
                Node next = node.children.get(p);
                if (next == null) {
                    next = new Node();
                    node.children.put(p, next);
                }
                node = next;
                ans += node.cnt;
            }
            node.cnt++;
        }
        return ans;
    }
}
