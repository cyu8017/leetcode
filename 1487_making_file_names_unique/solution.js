var getFolderNames = function(names) {
    const used = new Map(), result = [];
    for (const name of names) {
        if (!used.has(name)) {
            used.set(name, 1);
            result.push(name);
            continue;
        }
        let suffix = used.get(name);
        while (used.has(`${name}(${suffix})`)) suffix++;
        const unique = `${name}(${suffix})`;
        used.set(name, suffix + 1);
        used.set(unique, 1);
        result.push(unique);
    }
    return result;
};
