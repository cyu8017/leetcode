// LeetCode 0471 - Encode String with Shortest Length
// https://leetcode.com/problems/encode-string-with-shortest-length/

class Solution {
    public String encode(String s) {
        int length = s.length();
        String[] dp = new String[length + 1];

        for (int index = 1; index <= length; index++) {
            dp[index] = encodeWord(s.substring(0, index));
            for (int split = 1; split < index; split++) {
                String candidate = dp[index - split] + encodeWord(s.substring(index - split, index));
                if (candidate.length() < dp[index].length()
                        || (candidate.length() == dp[index].length() && candidate.compareTo(dp[index]) < 0)) {
                    dp[index] = candidate;
                }
            }
        }
        return dp[length];
    }

    private String encodeWord(String word) {
        int size = word.length();
        String best = word;
        for (int unitLength = 1; unitLength <= size / 2; unitLength++) {
            if (size % unitLength != 0) {
                continue;
            }
            String unit = word.substring(0, unitLength);
            StringBuilder repeated = new StringBuilder();
            for (int i = 0; i < size / unitLength; i++) {
                repeated.append(unit);
            }
            if (repeated.toString().equals(word)) {
                String encoded = (size / unitLength) + "[" + unit + "]";
                if (encoded.length() < best.length()
                        || (encoded.length() == best.length() && encoded.compareTo(best) < 0)) {
                    best = encoded;
                }
            }
        }
        return best;
    }
}
