// LeetCode 0751 - IP to CIDR
// https://leetcode.com/problems/ip-to-cidr/

export function ipToCIDR(ip: string, n: number): string[] {
    const ipToInt = (value) => {
        let result = 0;
        for (const part of value.split('.')) result = result * 256 + parseInt(part, 10);
        return result;
    };
    const intToIp = (value) => {
        return [
            Math.floor(value / 16777216) % 256,
            Math.floor(value / 65536) % 256,
            Math.floor(value / 256) % 256,
            value % 256
        ].join('.');
    };
    const bitLength = (value) => {
        let len = 0;
        while (value > 0) { value = Math.floor(value / 2); len++; }
        return len;
    };
    let start = ipToInt(ip);
    const answer = [];
    while (n > 0) {
        let lowbit = start === 0 ? Math.pow(2, 32) : (start & -start);
        // Convert signed 32-bit & result to unsigned
        if (start !== 0) {
            lowbit = start & -start;
            lowbit = lowbit >>> 0;
        }
        while (lowbit > n) lowbit = Math.floor(lowbit / 2);
        const mask = 32 - (bitLength(lowbit) - 1);
        answer.push(intToIp(start) + '/' + mask);
        start += lowbit;
        n -= lowbit;
    }
    return answer;
}
