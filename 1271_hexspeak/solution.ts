// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

function toHexspeak(num: string): string {
    let value = BigInt(num);
    const digits = '0123456789ABCDEF';
    let out = '';
    while (value > 0n) {
        const rem = Number(value % 16n);
        if (rem >= 2 && rem <= 9) return 'ERROR';
        out = digits[rem] + out;
        value = value / 16n;
    }
    return (out || '0').replace(/0/g, 'O').replace(/1/g, 'I');
}
