// LeetCode 0975 - Odd Even Jump
// https://leetcode.com/problems/odd-even-jump/

import java.util.*;

class Solution {
    public int oddEvenJumps(int[] arr) {
        int n = arr.length;
        int[] nextHigher = new int[n], nextLower = new int[n];
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, (i, j) -> arr[i] == arr[j] ? Integer.compare(i, j) : Integer.compare(arr[i], arr[j]));
        List<Integer> stack = new ArrayList<>();
        for (int i : order) {
            while (!stack.isEmpty() && stack.get(stack.size() - 1) < i) {
                nextHigher[stack.get(stack.size() - 1)] = i;
                stack.remove(stack.size() - 1);
            }
            stack.add(i);
        }
        stack.clear();
        Arrays.sort(order, (i, j) -> arr[i] == arr[j] ? Integer.compare(i, j) : Integer.compare(arr[j], arr[i]));
        for (int i : order) {
            while (!stack.isEmpty() && stack.get(stack.size() - 1) < i) {
                nextLower[stack.get(stack.size() - 1)] = i;
                stack.remove(stack.size() - 1);
            }
            stack.add(i);
        }
        boolean[] odd = new boolean[n], even = new boolean[n];
        odd[n - 1] = even[n - 1] = true;
        for (int i = n - 2; i >= 0; i--) {
            if (nextHigher[i] != 0) odd[i] = even[nextHigher[i]];
            if (nextLower[i] != 0) even[i] = odd[nextLower[i]];
        }
        int ans = 0;
        for (boolean x : odd) if (x) ans++;
        return ans;
    }
}
