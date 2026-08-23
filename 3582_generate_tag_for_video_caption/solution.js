// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

var generateTag = function(caption) {
    let ans = '#';
    const words = caption.trim().split(/\s+/);
    let i = 0;
    for (let word of words) {
        if (!word) continue;
        let w = word.toLowerCase();
        if (i === 0) ans += w;
        else {
            if (w.length > 0) w = w[0].toUpperCase() + w.slice(1);
            ans += w;
        }
        if (ans.length >= 100) break;
        i++;
    }
    if (ans.length > 100) ans = ans.substring(0, 100);
    return ans;
};
