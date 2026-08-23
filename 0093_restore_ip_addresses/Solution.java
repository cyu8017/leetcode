// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        List<String> path = new ArrayList<>();
        backtrack(s, 0, path, result);
        return result;
    }

    private void backtrack(String s, int start, List<String> path, List<String> result) {
        if (path.size() == 4) {
            if (start == s.length()) {
                result.add(String.join(".", path));
            }
            return;
        }

        for (int length = 1; length <= 3; length++) {
            if (start + length > s.length()) {
                break;
            }
            String part = s.substring(start, start + length);
            if ((part.startsWith("0") && part.length() > 1) || Integer.parseInt(part) > 255) {
                continue;
            }
            path.add(part);
            backtrack(s, start + length, path, result);
            path.remove(path.size() - 1);
        }
    }
}
