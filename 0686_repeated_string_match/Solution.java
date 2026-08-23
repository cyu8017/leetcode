// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

class Solution {
    public int repeatedStringMatch(String a, String b) {
        int repeats = (b.length() + a.length() - 1) / a.length();
        StringBuilder built = new StringBuilder(a.length() * (repeats + 1));
        for (int i = 0; i < repeats; i++) built.append(a);
        if (built.toString().contains(b)) return repeats;
        built.append(a);
        if (built.toString().contains(b)) return repeats + 1;
        return -1;
    }
}
