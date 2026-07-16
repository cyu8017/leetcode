// LeetCode 0076 - Minimum Window Substring
// https://leetcode.com/problems/minimum-window-substring/

export function minWindow(s: string, t: string): string {
    if (t.length === 0) {
        return "";
    }

    const need = new Map<string, number>();
    for (const ch of t) {
        need.set(ch, (need.get(ch) || 0) + 1);
    }

    const required = need.size;
    let formed = 0;
    const window = new Map<string, number>();
    let left = 0;
    let bestLen = Number.POSITIVE_INFINITY;
    let bestLeft = 0;

    for (let right = 0; right < s.length; right++) {
        const ch = s[right];
        window.set(ch, (window.get(ch) || 0) + 1);
        if (need.has(ch) && window.get(ch) === need.get(ch)) {
            formed++;
        }

        while (formed === required) {
            if (right - left + 1 < bestLen) {
                bestLen = right - left + 1;
                bestLeft = left;
            }

            const leftCh = s[left];
            window.set(leftCh, (window.get(leftCh) || 0) - 1);
            if (need.has(leftCh) && (window.get(leftCh) || 0) < (need.get(leftCh) || 0)) {
                formed--;
            }
            left++;
        }
    }

    if (bestLen === Number.POSITIVE_INFINITY) {
        return "";
    }

    return s.slice(bestLeft, bestLeft + bestLen);
}
