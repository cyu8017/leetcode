// LeetCode 1073 - Adding Two Negabinary Numbers
// https://leetcode.com/problems/adding-two-negabinary-numbers/

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] addNegabinary(int[] arr1, int[] arr2) {
        int i = arr1.length - 1, j = arr2.length - 1;
        int carry = 0;
        List<Integer> ans = new ArrayList<>();
        while (i >= 0 || j >= 0 || carry != 0) {
            int total = carry;
            if (i >= 0) {
                total += arr1[i--];
            }
            if (j >= 0) {
                total += arr2[j--];
            }
            ans.add(total & 1);
            carry = -(total >> 1);
        }
        while (ans.size() > 1 && ans.get(ans.size() - 1) == 0) {
            ans.remove(ans.size() - 1);
        }
        Collections.reverse(ans);
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
