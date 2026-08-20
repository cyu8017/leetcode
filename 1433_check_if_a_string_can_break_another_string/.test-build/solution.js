"use strict";
function checkIfCanBreak(s1, s2) {
    const a = [...s1].sort(), b = [...s2].sort();
    let ab = true, ba = true;
    for (let i = 0; i < a.length; i++) {
        if (a[i] < b[i])
            ab = false;
        if (b[i] < a[i])
            ba = false;
    }
    return ab || ba;
}
