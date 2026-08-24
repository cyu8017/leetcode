// LeetCode 0907 - Sum of Subarray Minimums
// https://leetcode.com/problems/sum-of-subarray-minimums/

export function sumSubarrayMins(arr: number[]): number {
    const MOD = 1000000007;
    const n = arr.length;
    const left = new Array(n).fill(-1);
    const right = new Array(n).fill(n);
    const st = [];
    for (let i = 0; i < n; i++) {
        while (st.length && arr[st[st.length - 1]] > arr[i]) st.pop();
        left[i] = st.length ? st[st.length - 1] : -1;
        st.push(i);
    }
    st.length = 0;
    for (let i = n - 1; i >= 0; i--) {
        while (st.length && arr[st[st.length - 1]] >= arr[i]) st.pop();
        right[i] = st.length ? st[st.length - 1] : n;
        st.push(i);
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        ans = (ans + arr[i] * (i - left[i]) * (right[i] - i)) % MOD;
    }
    return ans;
}
