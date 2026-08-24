// LeetCode 2227 - Encrypt and Decrypt Strings
// https://leetcode.com/problems/encrypt-and-decrypt-strings/

export class Encrypter {
    constructor(keys: string[], values: string[], dictionary: string[]) {
    this.enc = new Map();
    this.cnt = new Map();
    for (let i = 0; i < keys.length; i++) this.enc.set(keys[i], values[i]);
    for (const w of dictionary) {
        const e = this.encrypt(w);
        this.cnt.set(e, (this.cnt.get(e) || 0) + 1);
    }
}
    encrypt(word1: string): string {
    let b = '';
    for (const c of word1) {
        if (!this.enc.has(c)) return '';
        b += this.enc.get(c);
    }
    return b;
}
    decrypt(word2: string): number {
    return this.cnt.get(word2) || 0;
}
}
