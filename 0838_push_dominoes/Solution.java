// LeetCode 0838 - Push Dominoes
// https://leetcode.com/problems/push-dominoes/

class Solution {
    public String pushDominoes(String dominoes) {
        char[] arr = dominoes.toCharArray();
        int n = arr.length;
        int[] force = new int[n];
        int f = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == 'R') f = n;
            else if (arr[i] == 'L') f = 0;
            else f = Math.max(f - 1, 0);
            force[i] += f;
        }
        f = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (arr[i] == 'L') f = n;
            else if (arr[i] == 'R') f = 0;
            else f = Math.max(f - 1, 0);
            force[i] -= f;
        }
        for (int i = 0; i < n; i++) {
            if (force[i] > 0) arr[i] = 'R';
            else if (force[i] < 0) arr[i] = 'L';
            else arr[i] = '.';
        }
        return new String(arr);
    }
}
