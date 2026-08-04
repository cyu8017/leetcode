// LeetCode 1415: The K Th Lexicographical String Of All Happy Strings Of Length N

var getHappyString = function(n, k) {
    const build = (prefix, remaining) => {
        if (!remaining) { if (--k === 0) return prefix; return ""; }
        for (const ch of "abc") if (ch !== prefix.at(-1)) { const answer = build(prefix + ch, remaining - 1); if (answer) return answer; }
        return "";
    };
    return build("", n);
};
