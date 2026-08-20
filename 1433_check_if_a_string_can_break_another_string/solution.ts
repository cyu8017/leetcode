function checkIfCanBreak(s1: any, s2: any): any {
    const a = [...s1].sort(), b = [...s2].sort(); let ab = true, ba = true;
    for (let i = 0; i < a.length; i++) { if (a[i] < b[i]) ab = false; if (b[i] < a[i]) ba = false; }
    return ab || ba;
}
