// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

class Solution {
    public String decodeCiphertext(String encodedText, int rows) {
        if (rows == 1) return encodedText;
        int cols = encodedText.length() / rows;
        StringBuilder b = new StringBuilder();
        for (int c = 0; c < cols; c++)
            for (int r = 0; r < rows && c + r < cols; r++)
                b.append(encodedText.charAt(r * cols + c + r));
        while (b.length() > 0 && b.charAt(b.length() - 1) == ' ') b.setLength(b.length() - 1);
        return b.toString();
    }
}
