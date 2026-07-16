// LeetCode 0471 - Encode String with Shortest Length
// https://leetcode.com/problems/encode-string-with-shortest-length/

export class Solution {
    encode(s: string): string {
        const length = s.length;
        const dp = new Array<string>(length + 1).fill("");

        const encodeWord = (word: string): string => {
            const size = word.length;
            let best = word;
            for (let unitLength = 1; unitLength <= Math.floor(size / 2); unitLength += 1) {
                if (size % unitLength !== 0) continue;
                const unit = word.slice(0, unitLength);
                if (unit.repeat(size / unitLength) === word) {
                    const encoded = `${size / unitLength}[${unit}]`;
                    if (encoded.length < best.length || (encoded.length === best.length && encoded < best)) {
                        best = encoded;
                    }
                }
            }
            return best;
        };

        for (let index = 1; index <= length; index += 1) {
            dp[index] = encodeWord(s.slice(0, index));
            for (let split = 1; split < index; split += 1) {
                const candidate = dp[index - split] + encodeWord(s.slice(index - split, index));
                if (candidate.length < dp[index].length || (candidate.length === dp[index].length && candidate < dp[index])) {
                    dp[index] = candidate;
                }
            }
        }
        return dp[length];
    }
}
