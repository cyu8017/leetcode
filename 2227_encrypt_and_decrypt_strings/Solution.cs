// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

using System.Collections.Generic;
using System.Text;

public class Encrypter {
    Dictionary<char, string> enc = new Dictionary<char, string>();
    Dictionary<string, int> cnt = new Dictionary<string, int>();

    public Encrypter(char[] keys, string[] values, string[] dictionary) {
        for (int i = 0; i < keys.Length; i++) enc[keys[i]] = values[i];
        foreach (var w in dictionary) {
            string e = Encrypt(w);
            cnt.TryGetValue(e, out int c);
            cnt[e] = c + 1;
        }
    }

    public string Encrypt(string word1) {
        var b = new StringBuilder();
        foreach (char c in word1) {
            if (!enc.TryGetValue(c, out string v)) return "";
            b.Append(v);
        }
        return b.ToString();
    }

    public int Decrypt(string word2) {
        cnt.TryGetValue(word2, out int c);
        return c;
    }
}
