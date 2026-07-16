// LeetCode 0126 - Word Ladder II
// https://leetcode.com/problems/word-ladder-ii/

use std::collections::{HashMap, HashSet, VecDeque};
impl Solution {
    pub fn find_ladders(begin_word: String, end_word: String, word_list: Vec<String>) -> Vec<Vec<String>> {
        let words:HashSet<String>=word_list.into_iter().collect();if !words.contains(&end_word){return vec![]}
        let(mut parents,mut queue,mut seen)=(HashMap::<String,Vec<String>>::new(),VecDeque::from([begin_word.clone()]),HashSet::from([begin_word.clone()]));let mut found=false;
        while !queue.is_empty()&&!found{let mut level=HashSet::new();for _ in 0..queue.len(){let word=queue.pop_front().unwrap();let mut chars=word.into_bytes();for i in 0..chars.len(){let saved=chars[i];for c in b'a'..=b'z'{chars[i]=c;let next=String::from_utf8(chars.clone()).unwrap();if words.contains(&next)&&!seen.contains(&next){if level.insert(next.clone()){queue.push_back(next.clone());}parents.entry(next).or_default().push(word.clone());}}chars[i]=saved;}}seen.extend(level.iter().cloned());found=level.contains(&end_word);}
        if !found{return vec![]}let mut result=vec![];let mut path=vec![end_word.clone()];fn dfs(word:&str,begin:&str,parents:&HashMap<String,Vec<String>>,path:&mut Vec<String>,result:&mut Vec<Vec<String>>){if word==begin{let mut row=path.clone();row.reverse();result.push(row);return}if let Some(prev)=parents.get(word){for parent in prev{path.push(parent.clone());dfs(parent,begin,parents,path,result);path.pop();}}}dfs(&end_word,&begin_word,&parents,&mut path,&mut result);result.sort();result
    }
}