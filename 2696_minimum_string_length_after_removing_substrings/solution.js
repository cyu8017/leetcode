// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

var minLength = function(s) {
    const st = [];
    for (const c of s) {
        const last = st[st.length - 1];
        if (st.length && ((last === "A" && c === "B") || (last === "C" && c === "D")))
            st.pop();
        else st.push(c);
    }
    return st.length;
};
