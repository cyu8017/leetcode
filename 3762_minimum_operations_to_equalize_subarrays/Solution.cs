// LeetCode 3762 - Minimum Operations to Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/

using System;
using System.Collections.Generic;

public class Solution {
    class Node {
        public int Left, Right, Count;
        public long Sum;
    }

    public long[] MinOperations(int[] nums, int k, int[][] queries) {
        int n = nums.Length;
        int[] quotient = new int[n], remainder = new int[n], values = new int[n];
        for (int i = 0; i < n; i++) {
            quotient[i] = nums[i] / k;
            remainder[i] = nums[i] % k;
            values[i] = quotient[i];
        }
        Array.Sort(values);
        int vu = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || values[i] != values[i - 1]) values[vu++] = values[i];
        }
        Array.Resize(ref values, vu);
        var nodes = new List<Node> { new Node() };
        int Update(int previous, int lo, int hi, int position, int value) {
            int current = nodes.Count;
            var nn = new Node {
                Left = nodes[previous].Left,
                Right = nodes[previous].Right,
                Count = nodes[previous].Count,
                Sum = nodes[previous].Sum
            };
            nodes.Add(nn);
            nodes[current].Count++;
            nodes[current].Sum += value;
            if (lo < hi) {
                int mid = (lo + hi) / 2;
                if (position <= mid) nodes[current].Left = Update(nodes[previous].Left, lo, mid, position, value);
                else nodes[current].Right = Update(nodes[previous].Right, mid + 1, hi, position, value);
            }
            return current;
        }
        int[] roots = new int[n + 1];
        int umax = values.Length - 1;
        for (int i = 0; i < n; i++) {
            int position = LowerBound(values, quotient[i]);
            roots[i + 1] = Update(roots[i], 0, umax, position, quotient[i]);
        }
        int Kth(int rightRoot, int leftRoot, int lo, int hi, int rank) {
            if (lo == hi) return lo;
            int leftCount = nodes[nodes[rightRoot].Left].Count - nodes[nodes[leftRoot].Left].Count;
            int mid = (lo + hi) / 2;
            if (rank <= leftCount) return Kth(nodes[rightRoot].Left, nodes[leftRoot].Left, lo, mid, rank);
            return Kth(nodes[rightRoot].Right, nodes[leftRoot].Right, mid + 1, hi, rank - leftCount);
        }
        (int, long) PrefixStats(int rightRoot, int leftRoot, int lo, int hi, int end) {
            if (end < lo) return (0, 0);
            if (hi <= end) return (nodes[rightRoot].Count - nodes[leftRoot].Count,
                                   nodes[rightRoot].Sum - nodes[leftRoot].Sum);
            int mid = (lo + hi) / 2;
            var (count, sum) = PrefixStats(nodes[rightRoot].Left, nodes[leftRoot].Left, lo, mid, end);
            if (end > mid) {
                var (c2, s2) = PrefixStats(nodes[rightRoot].Right, nodes[leftRoot].Right, mid + 1, hi, end);
                count += c2;
                sum += s2;
            }
            return (count, sum);
        }
        int[] logv = new int[n + 1];
        for (int i = 2; i <= n; i++) logv[i] = logv[i / 2] + 1;
        int levels = logv[n] + 1;
        int[][] minTable = new int[levels][];
        int[][] maxTable = new int[levels][];
        minTable[0] = (int[])remainder.Clone();
        maxTable[0] = (int[])remainder.Clone();
        for (int level = 1; level < levels; level++) {
            int length = n - (1 << level) + 1;
            minTable[level] = new int[length];
            maxTable[level] = new int[length];
            int half = 1 << (level - 1);
            for (int i = 0; i < length; i++) {
                minTable[level][i] = Math.Min(minTable[level - 1][i], minTable[level - 1][i + half]);
                maxTable[level][i] = Math.Max(maxTable[level - 1][i], maxTable[level - 1][i + half]);
            }
        }
        long[] answer = new long[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int left = queries[qi][0], right = queries[qi][1];
            int length = right - left + 1;
            int level = logv[length];
            int offset = right - (1 << level) + 1;
            int minR = Math.Min(minTable[level][left], minTable[level][offset]);
            int maxR = Math.Max(maxTable[level][left], maxTable[level][offset]);
            if (minR != maxR) {
                answer[qi] = -1;
                continue;
            }
            int medianIndex = Kth(roots[right + 1], roots[left], 0, umax, (length + 1) / 2);
            int median = values[medianIndex];
            var (leftCount, leftSum) = PrefixStats(roots[right + 1], roots[left], 0, umax, medianIndex);
            long totalSum = nodes[roots[right + 1]].Sum - nodes[roots[left]].Sum;
            answer[qi] = 1L * median * leftCount - leftSum + (totalSum - leftSum) - 1L * median * (length - leftCount);
        }
        return answer;
    }

    static int LowerBound(int[] a, int x) {
        int lo = 0, hi = a.Length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
