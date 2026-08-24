// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

class Encrypter {
    private val enc = HashMap<Char, String>()
    private val cnt = HashMap<String, Int>()

    constructor(keys: CharArray, values: Array<String>, dictionary: Array<String>) {
        for (i in keys.indices) enc[keys[i]] = values[i]
        for (w in dictionary) {
            val e = encrypt(w)
            cnt[e] = cnt.getOrDefault(e, 0) + 1
        }
    }

    fun encrypt(word1: String): String {
        val b = StringBuilder()
        for (c in word1) {
            if (!enc.containsKey(c)) return ""
            b.append(enc[c])
        }
        return b.toString()
    }

    fun decrypt(word2: String): Int {
        return cnt.getOrDefault(word2, 0)
    }
}
