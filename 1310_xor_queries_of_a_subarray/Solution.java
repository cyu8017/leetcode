// LeetCode 1310 - Xor Queries Of A Subarray
// https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution {
    public int[] xorQueries(int[] arr, int[][] queries) {
        var prefix = new int[arr.length + 1];
        for (int i = 0; i < arr.length; i++) prefix[i + 1] = prefix[i] ^ arr[i];
        var answer = new int[queries.length];
        for (int i = 0; i < queries.length; i++)
            answer[i] = prefix[queries[i][1] + 1] ^ prefix[queries[i][0]];
        return answer;
    }
}
