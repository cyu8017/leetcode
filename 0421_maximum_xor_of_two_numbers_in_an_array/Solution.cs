// LeetCode 0421 - Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

using System.Collections.Generic;

public class Solution {
    private sealed class TrieNode {
        public Dictionary<int, TrieNode> Children = new();
    }

    public int FindMaximumXOR(int[] nums) {
        int maximum = int.MinValue;
        foreach (int number in nums) {
            maximum = int.Max(maximum, number);
        }
        int maxBit = maximum == 0 ? 0 : 32 - System.Numerics.BitOperations.LeadingZeroCount((uint)maximum);
        TrieNode root = new();
        int best = 0;

        foreach (int number in nums) {
            TrieNode node = root;
            for (int bit = maxBit - 1; bit >= 0; bit--) {
                int current = (number >> bit) & 1;
                if (!node.Children.ContainsKey(current)) {
                    node.Children[current] = new TrieNode();
                }
                node = node.Children[current];
            }
        }

        foreach (int number in nums) {
            TrieNode node = root;
            int candidate = 0;
            for (int bit = maxBit - 1; bit >= 0; bit--) {
                int current = (number >> bit) & 1;
                int target = 1 - current;
                if (node.Children.ContainsKey(target)) {
                    candidate |= 1 << bit;
                    node = node.Children[target];
                } else {
                    node = node.Children[current];
                }
            }
            best = int.Max(best, candidate);
        }

        return best;
    }
}
