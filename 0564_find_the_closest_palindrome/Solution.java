// LeetCode 0564 - Find the Closest Palindrome
// https://leetcode.com/problems/find-the-closest-palindrome/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String nearestPalindromic(String n) {
        int length = n.length();
        long number = Long.parseLong(n);
        List<Long> candidates = new ArrayList<>();
        candidates.add(pow10(length - 1) - 1);
        candidates.add(pow10(length) + 1);

        long prefix = Long.parseLong(n.substring(0, (length + 1) / 2));
        for (long half = prefix - 1; half <= prefix + 1; ++half) {
            candidates.add(makePalindrome(half, length));
        }

        long best = -1;
        long bestDiff = Long.MAX_VALUE;
        for (long candidate : candidates) {
            if (candidate == number) {
                continue;
            }
            long diff = Math.abs(candidate - number);
            if (diff < bestDiff || (diff == bestDiff && candidate < best)) {
                best = candidate;
                bestDiff = diff;
            }
        }
        return String.valueOf(best);
    }

    private long makePalindrome(long half, int length) {
        String text = String.valueOf(half);
        StringBuilder pal = new StringBuilder(text);
        if (length % 2 == 0) {
            for (int i = text.length() - 1; i >= 0; --i) {
                pal.append(text.charAt(i));
            }
        } else {
            for (int i = text.length() - 2; i >= 0; --i) {
                pal.append(text.charAt(i));
            }
        }
        return Long.parseLong(pal.toString());
    }

    private long pow10(int exp) {
        long value = 1;
        for (int i = 0; i < exp; ++i) {
            value *= 10;
        }
        return value;
    }
}
