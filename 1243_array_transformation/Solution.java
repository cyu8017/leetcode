// LeetCode 1243 - Array Transformation
// https://leetcode.com/problems/array-transformation/

import java.util.*;

class Solution {
    public List<Integer> transformArray(int[] arr) {
        while (true) {
            int[] nxt = arr.clone();
            for (int i = 1; i < arr.length - 1; i++) {
                if (arr[i] < arr[i - 1] && arr[i] < arr[i + 1]) nxt[i]++;
                else if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) nxt[i]--;
            }
            if (Arrays.equals(nxt, arr)) {
                List<Integer> answer = new ArrayList<>();
                for (int x : arr) answer.add(x);
                return answer;
            }
            arr = nxt;
        }
    }
}

