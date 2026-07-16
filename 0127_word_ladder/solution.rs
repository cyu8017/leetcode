// LeetCode 0127 - Word Ladder
// https://leetcode.com/problems/word-ladder/

use std::collections::{HashSet, VecDeque};
impl Solution { pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 { let words:HashSet<String>=word_list.into_iter().collect();if !words.contains(&end_word){return 0}let(mut queue,mut seen)=(VecDeque::from([(begin_word,1)]),HashSet::new());while let Some((word,steps))=queue.pop_front(){if word==end_word{return steps}let mut chars=word.into_bytes();for i in 0..chars.len(){let saved=chars[i];for c in b'a'..=b'z'{chars[i]=c;let next=String::from_utf8(chars.clone()).unwrap();if words.contains(&next)&&seen.insert(next.clone()){queue.push_back((next,steps+1));}}chars[i]=saved;}}0 } }