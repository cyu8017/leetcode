// LeetCode 1432 - Max Difference You Can Get From Changing An Integer
// https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

class Solution {
    public int maxDiff(int num) {
        String s = String.valueOf(num);
        char a = 0;
        for (char c : s.toCharArray()) {
            if (c != '9') {
                a = c;
                break;
            }
        }
        String max = a == 0 ? s : s.replace(a, '9');
        char b = s.charAt(0);
        String min;
        if (b != '1') {
            min = s.replace(b, '1');
        } else {
            char x = 0;
            for (int i = 1; i < s.length(); i++) {
                if (s.charAt(i) != '0' && s.charAt(i) != '1') {
                    x = s.charAt(i);
                    break;
                }
            }
            min = x == 0 ? s : s.replace(x, '0');
        }
        return Integer.parseInt(max) - Integer.parseInt(min);
    }
}
