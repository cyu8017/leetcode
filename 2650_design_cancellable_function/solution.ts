// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

export function cancellable(generator: any): any {
    let cancelled = false;
    const cancel = () => { cancelled = true; };
    const promise = (async () => {
        let next = generator.next();
        while (!next.done) {
            try {
                const value = await next.value;
                if (cancelled) {
                    next = generator.throw("Cancelled");
                    continue;
                }
                next = generator.next(value);
            } catch (e) {
                next = generator.throw(e);
            }
        }
        return next.value;
    })();
    return [cancel, promise];
}
