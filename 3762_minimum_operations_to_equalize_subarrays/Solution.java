// LeetCode 3762 - Minimum Operations To Equalize Subarrays
// https://leetcode.com/problems/minimum_operations_to_equalize_subarrays/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    static class Node {
        int left, right, count;
        long sum;
        Node() {}
        Node(Node o) {
            left = o.left; right = o.right; count = o.count; sum = o.sum;
        }
    }

    private List<Node> nodes;

    public long[] minOperations(int[] nums, int k, int[][] queries) {
        int n = nums.length;
        int[] quotient = new int[n], remainder = new int[n], values = new int[n];
        for (int i = 0; i < n; i++) {
            quotient[i] = nums[i] / k;
            remainder[i] = nums[i] % k;
            values[i] = quotient[i];
        }
        Arrays.sort(values);
        int vu = 1;
        for (int i = 1; i < n; i++) if (values[i] != values[vu - 1]) values[vu++] = values[i];
        values = Arrays.copyOf(values, vu);

        nodes = new ArrayList<>();
        nodes.add(new Node());
        int[] roots = new int[n + 1];
        int umax = values.length - 1;
        for (int i = 0; i < n; i++) {
            int position = lowerBound(values, quotient[i]);
            roots[i + 1] = update(roots[i], 0, umax, position, quotient[i]);
        }

        int[] logv = new int[n + 1];
        for (int i = 2; i <= n; i++) logv[i] = logv[i / 2] + 1;
        int levels = logv[n] + 1;
        int[][] minTable = new int[levels][];
        int[][] maxTable = new int[levels][];
        minTable[0] = remainder.clone();
        maxTable[0] = remainder.clone();
        for (int level = 1; level < levels; level++) {
            int length = n - (1 << level) + 1;
            minTable[level] = new int[length];
            maxTable[level] = new int[length];
            int half = 1 << (level - 1);
            for (int i = 0; i < length; i++) {
                minTable[level][i] = Math.min(minTable[level - 1][i], minTable[level - 1][i + half]);
                maxTable[level][i] = Math.max(maxTable[level - 1][i], maxTable[level - 1][i + half]);
            }
        }

        long[] answer = new long[queries.length];
        for (int qi = 0; qi < queries.length; qi++) {
            int left = queries[qi][0], right = queries[qi][1];
            int length = right - left + 1;
            int level = logv[length];
            int offset = right - (1 << level) + 1;
            int minR = Math.min(minTable[level][left], minTable[level][offset]);
            int maxR = Math.max(maxTable[level][left], maxTable[level][offset]);
            if (minR != maxR) {
                answer[qi] = -1;
                continue;
            }
            int medianIndex = kth(roots[right + 1], roots[left], 0, umax, (length + 1) / 2);
            int median = values[medianIndex];
            long[] stats = prefixStats(roots[right + 1], roots[left], 0, umax, medianIndex);
            int leftCount = (int) stats[0];
            long leftSum = stats[1];
            long totalSum = nodes.get(roots[right + 1]).sum - nodes.get(roots[left]).sum;
            answer[qi] = 1L * median * leftCount - leftSum + (totalSum - leftSum) - 1L * median * (length - leftCount);
        }
        return answer;
    }

    private int update(int previous, int lo, int hi, int position, int value) {
        int current = nodes.size();
        nodes.add(new Node(nodes.get(previous)));
        nodes.get(current).count++;
        nodes.get(current).sum += value;
        if (lo < hi) {
            int mid = (lo + hi) / 2;
            if (position <= mid) nodes.get(current).left = update(nodes.get(previous).left, lo, mid, position, value);
            else nodes.get(current).right = update(nodes.get(previous).right, mid + 1, hi, position, value);
        }
        return current;
    }

    private int kth(int rightRoot, int leftRoot, int lo, int hi, int rank) {
        if (lo == hi) return lo;
        int leftCount = nodes.get(nodes.get(rightRoot).left).count - nodes.get(nodes.get(leftRoot).left).count;
        int mid = (lo + hi) / 2;
        if (rank <= leftCount) return kth(nodes.get(rightRoot).left, nodes.get(leftRoot).left, lo, mid, rank);
        return kth(nodes.get(rightRoot).right, nodes.get(leftRoot).right, mid + 1, hi, rank - leftCount);
    }

    private long[] prefixStats(int rightRoot, int leftRoot, int lo, int hi, int end) {
        if (end < lo) return new long[]{0, 0};
        if (hi <= end) return new long[]{
            nodes.get(rightRoot).count - nodes.get(leftRoot).count,
            nodes.get(rightRoot).sum - nodes.get(leftRoot).sum
        };
        int mid = (lo + hi) / 2;
        long[] left = prefixStats(nodes.get(rightRoot).left, nodes.get(leftRoot).left, lo, mid, end);
        long count = left[0], sum = left[1];
        if (end > mid) {
            long[] right = prefixStats(nodes.get(rightRoot).right, nodes.get(leftRoot).right, mid + 1, hi, end);
            count += right[0];
            sum += right[1];
        }
        return new long[]{count, sum};
    }

    private int lowerBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
