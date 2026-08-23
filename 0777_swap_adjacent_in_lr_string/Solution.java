// LeetCode 0777 - Swap Adjacent in LR String
// https://leetcode.com/problems/swap-adjacent-in-lr-string/

class Solution {
    public boolean canTransform(String start, String result) {
        StringBuilder a = new StringBuilder();
        StringBuilder b = new StringBuilder();
        for (char ch : start.toCharArray()) if (ch != 'X') a.append(ch);
        for (char ch : result.toCharArray()) if (ch != 'X') b.append(ch);
        if (!a.toString().equals(b.toString())) return false;
        int i = 0, j = 0, n = start.length();
        while (i < n && j < n) {
            while (i < n && start.charAt(i) == 'X') i++;
            while (j < n && result.charAt(j) == 'X') j++;
            if (i == n || j == n) break;
            if (start.charAt(i) != result.charAt(j)) return false;
            if (start.charAt(i) == 'L' && i < j) return false;
            if (start.charAt(i) == 'R' && i > j) return false;
            i++;
            j++;
        }
        return true;
    }
}
