// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

/**
 * @param {any} poly1
 * @param {any} poly2
 * @return {any}
 */
var addPoly = function(poly1, poly2) {
    const listMode = Array.isArray(poly1) || Array.isArray(poly2);
    const build = (items) => {
        const dummy = { coefficient: 0, power: 0, next: null };
        let cur = dummy;
        for (const [c, p] of items) {
            cur.next = { coefficient: c, power: p, next: null };
            cur = cur.next;
        }
        return dummy.next;
    };
    if (Array.isArray(poly1)) poly1 = build(poly1);
    if (Array.isArray(poly2)) poly2 = build(poly2);
    const dummy = { coefficient: 0, power: 0, next: null };
    let cur = dummy;
    while (poly1 || poly2) {
        let c, p;
        if (!poly2 || (poly1 && poly1.power > poly2.power)) {
            c = poly1.coefficient; p = poly1.power; poly1 = poly1.next;
        } else if (!poly1 || poly2.power > poly1.power) {
            c = poly2.coefficient; p = poly2.power; poly2 = poly2.next;
        } else {
            c = poly1.coefficient + poly2.coefficient; p = poly1.power;
            poly1 = poly1.next; poly2 = poly2.next;
        }
        if (c) {
            cur.next = { coefficient: c, power: p, next: null };
            cur = cur.next;
        }
    }
    if (!listMode) return dummy.next;
    const out = [];
    cur = dummy.next;
    while (cur) {
        out.push([cur.coefficient, cur.power]);
        cur = cur.next;
    }
    return out;
};
