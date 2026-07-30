// LeetCode 1310 - Xor Queries Of A Subarray
// https://leetcode.com/problems/xor-queries-of-a-subarray/

public class Solution {
    public int[] XorQueries(int[] arr, int[][] queries) {
        var prefix = new int[arr.Length + 1];
        for (int i = 0; i < arr.Length; i++) prefix[i + 1] = prefix[i] ^ arr[i];
        var answer = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++)
            answer[i] = prefix[queries[i][1] + 1] ^ prefix[queries[i][0]];
        return answer;
    }
}
