// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int countPairs(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (almostEqual(nums[i], nums[j])) ans++;
            }
        }
        return ans;
    }

    private String sprintfNum(int x) {
        if (x == 0) return "0";
        StringBuilder b = new StringBuilder();
        while (x > 0) {
            b.insert(0, (char) ('0' + x % 10));
            x /= 10;
        }
        return b.toString();
    }

    private boolean almostEqual(int a, int b) {
        String sa = sprintfNum(a), sb = sprintfNum(b);
        while (sa.length() < sb.length()) sa = "0" + sa;
        while (sb.length() < sa.length()) sb = "0" + sb;
        List<Integer> diff = new ArrayList<>();
        for (int i = 0; i < sa.length(); i++) {
            if (sa.charAt(i) != sb.charAt(i)) diff.add(i);
        }
        if (diff.isEmpty()) return true;
        if (diff.size() != 2) return false;
        int i0 = diff.get(0), j = diff.get(1);
        return sa.charAt(i0) == sb.charAt(j) && sa.charAt(j) == sb.charAt(i0);
    }
}
