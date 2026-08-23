// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

import java.util.*;

class Solution {
    public int[] findEvenNumbers(int[] digits) {
        int[] freq = new int[10];
        for (int d : digits) freq[d]++;
        List<Integer> ans = new ArrayList<>();
        for (int x = 100; x <= 998; x += 2) {
            int a = x / 100, b = (x / 10) % 10, c = x % 10;
            freq[a]--; freq[b]--; freq[c]--;
            if (freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0) ans.add(x);
            freq[a]++; freq[b]++; freq[c]++;
        }
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }
}
