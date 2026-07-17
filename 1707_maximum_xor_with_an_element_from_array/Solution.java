// LeetCode 1707 - Maximum XOR With an Element From Array
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

import java.util.Arrays;

class Solution {
    private int[][] children;
    private int nodeCount;

    public int[] maximizeXor(int[] nums, int[][] queries) {
        Arrays.sort(nums);
        Integer[] order = new Integer[queries.length];
        for (int i = 0; i < queries.length; i++) {
            order[i] = i;
        }
        Arrays.sort(order, (a, b) -> Integer.compare(queries[a][1], queries[b][1]));

        children = new int[nums.length * 32 + 1][2];
        for (int[] node : children) {
            node[0] = -1;
            node[1] = -1;
        }
        nodeCount = 1;

        int[] ans = new int[queries.length];
        Arrays.fill(ans, -1);
        int added = 0;
        for (int qi : order) {
            int x = queries[qi][0];
            int limit = queries[qi][1];
            while (added < nums.length && nums[added] <= limit) {
                insert(nums[added]);
                added++;
            }
            if (added == 0) {
                continue;
            }
            int node = 0;
            int value = 0;
            for (int bit = 31; bit >= 0; bit--) {
                int b = (x >> bit) & 1;
                int want = b ^ 1;
                if (children[node][want] != -1) {
                    value |= 1 << bit;
                    node = children[node][want];
                } else {
                    node = children[node][b];
                }
            }
            ans[qi] = value;
        }
        return ans;
    }

    private void insert(int num) {
        int node = 0;
        for (int bit = 31; bit >= 0; bit--) {
            int b = (num >> bit) & 1;
            if (children[node][b] == -1) {
                children[node][b] = nodeCount++;
            }
            node = children[node][b];
        }
    }
}
