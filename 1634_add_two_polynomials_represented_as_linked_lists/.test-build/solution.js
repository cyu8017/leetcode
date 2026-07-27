"use strict";
// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/
function addPoly(poly1, poly2) {
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
    let p1 = Array.isArray(poly1) ? build(poly1) : poly1;
    let p2 = Array.isArray(poly2) ? build(poly2) : poly2;
    const dummy = { coefficient: 0, power: 0, next: null };
    let cur = dummy;
    while (p1 || p2) {
        let c, p;
        if (!p2 || (p1 && p1.power > p2.power)) {
            c = p1.coefficient;
            p = p1.power;
            p1 = p1.next;
        }
        else if (!p1 || p2.power > p1.power) {
            c = p2.coefficient;
            p = p2.power;
            p2 = p2.next;
        }
        else {
            c = p1.coefficient + p2.coefficient;
            p = p1.power;
            p1 = p1.next;
            p2 = p2.next;
        }
        if (c) {
            cur.next = { coefficient: c, power: p, next: null };
            cur = cur.next;
        }
    }
    if (!listMode)
        return dummy.next;
    const out = [];
    let node = dummy.next;
    while (node) {
        out.push([node.coefficient, node.power]);
        node = node.next;
    }
    return out;
}
