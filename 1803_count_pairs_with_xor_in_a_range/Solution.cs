// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

public class Solution {
    private class TrieNode {
        public int Count;
        public readonly TrieNode[] Children = new TrieNode[2];
    }

    public int CountPairs(int[] nums, int low, int high) {
        return CountSmallerThan(nums, high + 1) - CountSmallerThan(nums, low);
    }

    private int CountSmallerThan(int[] nums, int limit) {
        if (limit <= 0) return 0;
        var root = new TrieNode();
        int total = 0;
        const int maxBit = 15;
        foreach (int num in nums) {
            total += Query(root, num, limit, maxBit);
            Insert(root, num, maxBit);
        }
        return total;
    }

    private void Insert(TrieNode root, int num, int bit) {
        var node = root;
        for (int i = bit; i >= 0; i--) {
            int b = (num >> i) & 1;
            if (node.Children[b] == null) node.Children[b] = new TrieNode();
            node = node.Children[b];
            node.Count++;
        }
    }

    private int Query(TrieNode root, int num, int limit, int bit) {
        if (root == null || bit < 0) return 0;
        int numBit = (num >> bit) & 1;
        int limitBit = (limit >> bit) & 1;
        var child = root.Children[numBit];
        if (limitBit == 1) {
            int result = child != null ? child.Count : 0;
            result += Query(root.Children[1 - numBit], num, limit, bit - 1);
            return result;
        }
        return Query(child, num, limit, bit - 1);
    }
}
