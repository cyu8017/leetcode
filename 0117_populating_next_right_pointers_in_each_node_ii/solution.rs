use std::cell::RefCell; use std::rc::Rc;
#[derive(Debug)] pub struct Node { pub val:i32, pub left:Option<Rc<RefCell<Node>>>, pub right:Option<Rc<RefCell<Node>>>, pub next:Option<Rc<RefCell<Node>>> }
impl Node { pub fn new(val:i32)->Self { Self { val,left:None,right:None,next:None } } }
impl Solution { pub fn connect(root:Option<Rc<RefCell<Node>>>) -> Option<Rc<RefCell<Node>>> {
    let Some(r)=root.clone() else{return None}; let mut q=vec![r]; let mut head=0;
    while head<q.len() { let end=q.len(); let mut prev=None;
        while head<end { let n=q[head].clone(); head+=1; if let Some(p)=prev { p.borrow_mut().next=Some(n.clone()); }
            let x=n.borrow(); if let Some(l)=x.left.clone(){q.push(l)} if let Some(r)=x.right.clone(){q.push(r)} prev=Some(n); }
        if let Some(p)=prev { p.borrow_mut().next=None; }
    } root
} }