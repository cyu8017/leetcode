// LeetCode 3991 - Sort Array Using Prefix Reversals
// https://leetcode.com/problems/sort-array-using-prefix-reversals/

import java.util.*;

class Solution {
    public int sortArray(int[] nums, int[] pre) {
        int n = nums.length;
        String start = key(nums);
        int[] targetArr = new int[n];
        for (int i = 0; i < n; i++) targetArr[i] = i;
        String target = key(targetArr);
        if (start.equals(target)) return 0;

        TreeSet<Integer> lengthSet = new TreeSet<>();
        for (int i : pre) {
            if (i >= 2 && i <= n) lengthSet.add(i);
        }
        List<Integer> lengths = new ArrayList<>(lengthSet);

        Set<String> visited = new HashSet<>();
        visited.add(start);
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(nums.clone());
        int steps = 0;

        while (!queue.isEmpty()) {
            steps++;
            int size = queue.size();
            for (int q = 0; q < size; q++) {
                int[] cur = queue.poll();
                for (int i : lengths) {
                    int[] nxt = cur.clone();
                    for (int l = 0, r = i - 1; l < r; l++, r--) {
                        int tmp = nxt[l];
                        nxt[l] = nxt[r];
                        nxt[r] = tmp;
                    }
                    String k = key(nxt);
                    if (k.equals(target)) return steps;
                    if (visited.add(k)) queue.offer(nxt);
                }
            }
        }
        return -1;
    }

    private String key(int[] arr) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            if (i > 0) sb.append(',');
            sb.append(arr[i]);
        }
        return sb.toString();
    }
}
