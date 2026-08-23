// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

using System.Collections.Generic;

public class Solution {
    class Node {
        public int[] Next = new int[2];
        public int Count;
    }

    List<Node> nodes = new List<Node>();

    void Add(int x, int delta) {
        int u = 0;
        nodes[u].Count += delta;
        for (int b = 15; b >= 0; b--) {
            int bit = (x >> b) & 1;
            if (nodes[u].Next[bit] == 0) {
                nodes[u].Next[bit] = nodes.Count;
                nodes.Add(new Node());
            }
            u = nodes[u].Next[bit];
            nodes[u].Count += delta;
        }
    }

    int Query(int x) {
        int u = 0, res = 0;
        for (int b = 15; b >= 0; b--) {
            int bit = (x >> b) & 1;
            int want = bit ^ 1;
            int v = nodes[u].Next[want];
            if (v != 0 && nodes[v].Count > 0) {
                res |= 1 << b;
                u = v;
            } else {
                u = nodes[u].Next[bit];
            }
        }
        return res;
    }

    public int MaxSubarrayXor(int[] nums, int k) {
        nodes = new List<Node> { new Node() };
        int n = nums.Length;
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] ^ nums[i];
        var maxQ = new List<int>();
        var minQ = new List<int>();
        int left = 0, trieLeft = 0, ans = 0;
        for (int r = 0; r < n; r++) {
            int x = nums[r];
            while (maxQ.Count > 0 && nums[maxQ[maxQ.Count - 1]] <= x) maxQ.RemoveAt(maxQ.Count - 1);
            maxQ.Add(r);
            while (minQ.Count > 0 && nums[minQ[minQ.Count - 1]] >= x) minQ.RemoveAt(minQ.Count - 1);
            minQ.Add(r);
            while (nums[maxQ[0]] - nums[minQ[0]] > k) {
                if (maxQ[0] == left) maxQ.RemoveAt(0);
                if (minQ[0] == left) minQ.RemoveAt(0);
                left++;
            }
            Add(pref[r], 1);
            while (trieLeft < left) {
                Add(pref[trieLeft], -1);
                trieLeft++;
            }
            int cur = Query(pref[r + 1]);
            if (cur > ans) ans = cur;
        }
        return ans;
    }
}
