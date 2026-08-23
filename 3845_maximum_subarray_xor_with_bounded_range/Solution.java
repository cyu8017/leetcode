// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

import java.util.ArrayList;
import java.util.List;

class Solution {
    static class Node {
        int[] next = new int[2];
        int count;
    }

    private List<Node> nodes;

    private void add(int x, int delta) {
        int u = 0;
        nodes.get(u).count += delta;
        for (int b = 15; b >= 0; b--) {
            int bit = (x >> b) & 1;
            if (nodes.get(u).next[bit] == 0) {
                nodes.get(u).next[bit] = nodes.size();
                nodes.add(new Node());
            }
            u = nodes.get(u).next[bit];
            nodes.get(u).count += delta;
        }
    }

    private int query(int x) {
        int u = 0, res = 0;
        for (int b = 15; b >= 0; b--) {
            int bit = (x >> b) & 1;
            int want = bit ^ 1;
            int v = nodes.get(u).next[want];
            if (v != 0 && nodes.get(v).count > 0) {
                res |= 1 << b;
                u = v;
            } else {
                u = nodes.get(u).next[bit];
            }
        }
        return res;
    }

    public int maxSubarrayXor(int[] nums, int k) {
        nodes = new ArrayList<>();
        nodes.add(new Node());
        int n = nums.length;
        int[] pref = new int[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] ^ nums[i];
        List<Integer> maxQ = new ArrayList<>();
        List<Integer> minQ = new ArrayList<>();
        int left = 0, trieLeft = 0, ans = 0;
        for (int r = 0; r < n; r++) {
            int x = nums[r];
            while (!maxQ.isEmpty() && nums[maxQ.get(maxQ.size() - 1)] <= x) maxQ.remove(maxQ.size() - 1);
            maxQ.add(r);
            while (!minQ.isEmpty() && nums[minQ.get(minQ.size() - 1)] >= x) minQ.remove(minQ.size() - 1);
            minQ.add(r);
            while (nums[maxQ.get(0)] - nums[minQ.get(0)] > k) {
                if (maxQ.get(0) == left) maxQ.remove(0);
                if (minQ.get(0) == left) minQ.remove(0);
                left++;
            }
            add(pref[r], 1);
            while (trieLeft < left) {
                add(pref[trieLeft], -1);
                trieLeft++;
            }
            int cur = query(pref[r + 1]);
            if (cur > ans) ans = cur;
        }
        return ans;
    }
}
