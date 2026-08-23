// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

/**
 * @param {string} code
 * @return {boolean}
 */
var isValid = function(code) {
    const stack = [];
    let i = 0;
    const n = code.length;
    while (i < n) {
        if (code.startsWith("<![CDATA[", i)) {
            if (!stack.length) return false;
            const j = code.indexOf("]]>", i + 9);
            if (j < 0) return false;
            i = j + 3;
        } else if (code.startsWith("</", i)) {
            const j = code.indexOf(">", i + 2);
            if (j < 0) return false;
            const tag = code.substring(i + 2, j);
            if (!stack.length || stack[stack.length - 1] !== tag) return false;
            stack.pop();
            i = j + 1;
            if (!stack.length && i < n) return false;
        } else if (code[i] === "<") {
            const j = code.indexOf(">", i + 1);
            if (j < 0) return false;
            const tag = code.substring(i + 1, j);
            if (!tag.length || tag.length > 9) return false;
            for (let k = 0; k < tag.length; ++k) {
                const ch = tag.charCodeAt(k);
                if (ch < 65 || ch > 90) return false;
            }
            stack.push(tag);
            i = j + 1;
        } else {
            if (!stack.length) return false;
            ++i;
        }
    }
    return stack.length === 0;
};
