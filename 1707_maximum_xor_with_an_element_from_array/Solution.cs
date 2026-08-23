// LeetCode 1707 - Maximum XOR With an Element From Array
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

public class Solution {
    public int[] MaximizeXor(int[] nums, int[][] queries) {
        Array.Sort(nums);
        int[] order = new int[queries.Length];
        for (int i = 0; i < order.Length; i++) {
            order[i] = i;
        }
        Array.Sort(order, (a, b) => queries[a][1].CompareTo(queries[b][1]));

        var children = new List<int[]> { new int[] { -1, -1 } };

        void Insert(int num) {
            int node = 0;
            for (int bit = 31; bit >= 0; bit--) {
                int b = (num >> bit) & 1;
                if (children[node][b] == -1) {
                    children[node][b] = children.Count;
                    children.Add(new int[] { -1, -1 });
                }
                node = children[node][b];
            }
        }

        int[] ans = new int[queries.Length];
        Array.Fill(ans, -1);
        int added = 0;
        foreach (int qi in order) {
            int x = queries[qi][0];
            int limit = queries[qi][1];
            while (added < nums.Length && nums[added] <= limit) {
                Insert(nums[added]);
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
}
