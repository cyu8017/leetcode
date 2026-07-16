class Solution {
    public boolean isOneEditDistance(String s, String t) {
        if (Math.abs(s.length() - t.length()) > 1 || s.equals(t)) return false;
        if (s.length() > t.length()) { String temp = s; s = t; t = temp; }
        int i = 0;
        while (i < s.length() && s.charAt(i) == t.charAt(i)) i++;
        return s.length() == t.length() ? s.substring(i + 1).equals(t.substring(i + 1)) : s.substring(i).equals(t.substring(i + 1));
    }
}