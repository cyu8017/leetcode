// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

using System;
using System.Linq;

public class Solution {
    public int EarliestAcq(int[][] logs, int n) {
        int[] parent = Enumerable.Range(0, n).ToArray();

        int Find(int x) {
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }

        bool Unite(int a, int b) {
            int ra = Find(a);
            int rb = Find(b);
            if (ra == rb) {
                return false;
            }
            parent[rb] = ra;
            return true;
        }

        Array.Sort(logs, (a, b) => a[0].CompareTo(b[0]));
        int components = n;
        foreach (var log in logs) {
            if (Unite(log[1], log[2])) {
                components--;
                if (components == 1) {
                    return log[0];
                }
            }
        }
        return -1;
    }
}
