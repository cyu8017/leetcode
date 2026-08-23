// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

using System.Text;

public class Solution {
    public string DecodeCiphertext(string encodedText, int rows) {
        if (rows == 1) return encodedText;
        int cols = encodedText.Length / rows;
        var b = new StringBuilder();
        for (int c = 0; c < cols; c++)
            for (int r = 0; r < rows && c + r < cols; r++)
                b.Append(encodedText[r * cols + c + r]);
        while (b.Length > 0 && b[b.Length - 1] == ' ') b.Length--;
        return b.ToString();
    }
}
