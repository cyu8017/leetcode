// LeetCode 0271 - Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/

export class Codec {
    encode(strs: string[]): string {
        return strs.map((text) => `${text.length}#${text}`).join("");
    }

    decode(encoded: string): string[] {
        const result: string[] = [];
        let index = 0;
        while (index < encoded.length) {
            const delimiter = encoded.indexOf("#", index);
            const length = parseInt(encoded.slice(index, delimiter), 10);
            const start = delimiter + 1;
            result.push(encoded.slice(start, start + length));
            index = start + length;
        }
        return result;
    }
}

export function encode(strs: string[]): string {
    return new Codec().encode(strs);
}
