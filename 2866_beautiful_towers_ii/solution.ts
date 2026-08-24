// LeetCode 2866 - Beautiful Towers II
// https://leetcode.com/problems/beautiful-towers-ii/

export function maximumSumOfHeights(maxHeights: number[]): number {
    const n = maxHeights.length;
    const left = Array(n);
    let st = [-1];
    let sum = 0;
    for (let i = 0; i < n; i++) {
        while (st.length > 1 && maxHeights[st[st.length - 1]] >= maxHeights[i]) {
            const j = st.pop();
            sum -= maxHeights[j] * (j - st[st.length - 1]);
        }
        sum += maxHeights[i] * (i - st[st.length - 1]);
        left[i] = sum;
        st.push(i);
    }
    const right = Array(n);
    st = [n];
    sum = 0;
    for (let i = n - 1; i >= 0; i--) {
        while (st.length > 1 && maxHeights[st[st.length - 1]] >= maxHeights[i]) {
            const j = st.pop();
            sum -= maxHeights[j] * (st[st.length - 1] - j);
        }
        sum += maxHeights[i] * (st[st.length - 1] - i);
        right[i] = sum;
        st.push(i);
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const cand = left[i] + right[i] - maxHeights[i];
        if (cand > ans) ans = cand;
    }
    return ans;
}
