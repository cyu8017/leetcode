// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

import java.util.HashMap;
import java.util.Map;

class Encrypter {
    Map<Character, String> enc = new HashMap<>();
    Map<String, Integer> cnt = new HashMap<>();

    public Encrypter(char[] keys, String[] values, String[] dictionary) {
        for (int i = 0; i < keys.length; i++) enc.put(keys[i], values[i]);
        for (String w : dictionary) {
            String e = encrypt(w);
            cnt.put(e, cnt.getOrDefault(e, 0) + 1);
        }
    }

    public String encrypt(String word1) {
        StringBuilder b = new StringBuilder();
        for (char c : word1.toCharArray()) {
            if (!enc.containsKey(c)) return "";
            b.append(enc.get(c));
        }
        return b.toString();
    }

    public int decrypt(String word2) {
        return cnt.getOrDefault(word2, 0);
    }
}
