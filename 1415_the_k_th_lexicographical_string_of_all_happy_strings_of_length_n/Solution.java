// LeetCode 1415 - The K Th Lexicographical String Of All Happy Strings Of Length N
// https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

import java.util.*;

class Solution {
    public String getHappyString(int n, int k) {
        List<String> answer = new ArrayList<>();
        build("", n, answer);
        return k <= answer.size() ? answer.get(k - 1) : "";
    }

    private void build(String path, int n, List<String> answer) {
        if (path.length() == n) {
            answer.add(path);
            return;
        }
        for (char c : new char[]{'a', 'b', 'c'}) {
            if (path.isEmpty() || path.charAt(path.length() - 1) != c) {
                build(path + c, n, answer);
            }
        }
    }
}
