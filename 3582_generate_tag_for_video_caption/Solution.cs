// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

using System.Text;

public class Solution {
    public string GenerateTag(string caption) {
        var words = caption.Split((char[])null, System.StringSplitOptions.RemoveEmptyEntries);
        var ans = new StringBuilder("#");
        int i = 0;
        foreach (string w0 in words) {
            var word = w0.ToLowerInvariant().ToCharArray();
            if (i == 0) ans.Append(word);
            else {
                if (word.Length > 0) word[0] = char.ToUpperInvariant(word[0]);
                ans.Append(word);
            }
            if (ans.Length >= 100) break;
            i++;
        }
        if (ans.Length > 100) ans.Length = 100;
        return ans.ToString();
    }
}
