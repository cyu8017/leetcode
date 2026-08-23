// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

class Solution {
    private static class TrieNode {
        int count;
        TrieNode[] children = new TrieNode[2];
    }

    public int countPairs(int[] nums, int low, int high) {
        return countSmallerThan(nums, high + 1) - countSmallerThan(nums, low);
    }

    private int countSmallerThan(int[] nums, int limit) {
        if (limit <= 0) {
            return 0;
        }

        TrieNode root = new TrieNode();
        int total = 0;
        int maxBit = 15;

        for (int num : nums) {
            total += query(root, num, limit, maxBit);
            insert(root, num, maxBit);
        }
        return total;
    }

    private void insert(TrieNode root, int num, int bit) {
        TrieNode node = root;
        for (int i = bit; i >= 0; i--) {
            int b = (num >> i) & 1;
            if (node.children[b] == null) {
                node.children[b] = new TrieNode();
            }
            node = node.children[b];
            node.count++;
        }
    }

    private int query(TrieNode root, int num, int limit, int bit) {
        if (root == null || bit < 0) {
            return 0;
        }

        int numBit = (num >> bit) & 1;
        int limitBit = (limit >> bit) & 1;
        TrieNode child = root.children[numBit];

        if (limitBit == 1) {
            int result = child != null ? child.count : 0;
            result += query(root.children[1 - numBit], num, limit, bit - 1);
            return result;
        }
        return query(child, num, limit, bit - 1);
    }
}
