// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

export function restoreIpAddresses(s: string): string[] {
    const result: string[] = [];
    const path: string[] = [];

    function backtrack(start: number): void {
        if (path.length === 4) {
            if (start === s.length) {
                result.push(path.join('.'));
            }
            return;
        }

        for (let length = 1; length <= 3; length++) {
            if (start + length > s.length) {
                break;
            }
            const part = s.substring(start, start + length);
            if ((part.startsWith('0') && part.length > 1) || parseInt(part, 10) > 255) {
                continue;
            }
            path.push(part);
            backtrack(start + length);
            path.pop();
        }
    }

    backtrack(0);
    return result;
}
