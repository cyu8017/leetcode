// LeetCode 3606 - Coupon Code Validator
// https://leetcode.com/problems/coupon-code-validator/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<String> validateCoupons(String[] code, String[] businessLine, boolean[] isActive) {
        Set<String> bs = new HashSet<>();
        Collections.addAll(bs, "electronics", "grocery", "pharmacy", "restaurant");
        List<Integer> idx = new ArrayList<>();
        for (int i = 0; i < code.length; i++) {
            if (isActive[i] && bs.contains(businessLine[i]) && check(code[i])) idx.add(i);
        }
        idx.sort((i, j) -> {
            int c = businessLine[i].compareTo(businessLine[j]);
            if (c != 0) return c;
            return code[i].compareTo(code[j]);
        });
        List<String> ans = new ArrayList<>();
        for (int i : idx) ans.add(code[i]);
        return ans;
    }

    boolean check(String s) {
        if (s.isEmpty()) return false;
        for (char c : s.toCharArray())
            if (!Character.isLetterOrDigit(c) && c != '_') return false;
        return true;
    }
}
