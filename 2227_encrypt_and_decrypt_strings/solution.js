// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

/**
 * @param {character[]} keys
 * @param {string[]} values
 * @param {string[]} dictionary
 */
var Encrypter = function(keys, values, dictionary) {
    this.enc = new Map();
    this.cnt = new Map();
    for (let i = 0; i < keys.length; i++) this.enc.set(keys[i], values[i]);
    for (const w of dictionary) {
        const e = this.encrypt(w);
        this.cnt.set(e, (this.cnt.get(e) || 0) + 1);
    }
};

/** 
 * @param {string} word1
 * @return {string}
 */
Encrypter.prototype.encrypt = function(word1) {
    let b = '';
    for (const c of word1) {
        if (!this.enc.has(c)) return '';
        b += this.enc.get(c);
    }
    return b;
};

/** 
 * @param {string} word2
 * @return {number}
 */
Encrypter.prototype.decrypt = function(word2) {
    return this.cnt.get(word2) || 0;
};
