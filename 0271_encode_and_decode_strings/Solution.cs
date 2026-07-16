// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

using System.Collections.Generic;
using System.Text;

public class Codec {
    public string Encode(IList<string> strs) {
        var encoded = new StringBuilder();
        foreach (string text in strs) {
            encoded.Append(text.Length).Append('#').Append(text);
        }
        return encoded.ToString();
    }

    public IList<string> Decode(string encoded) {
        var result = new List<string>();
        int index = 0;
        while (index < encoded.Length) {
            int delimiter = encoded.IndexOf('#', index);
            int length = int.Parse(encoded.Substring(index, delimiter - index));
            int start = delimiter + 1;
            result.Add(encoded.Substring(start, length));
            index = start + length;
        }
        return result;
    }
}
